# step2: 리뷰 전체에 대해 형태소 분석하기 (skip)
import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, LongType, DateType, IntegerType
import pyspark.sql.functions as f
from pyspark.sql import SparkSession


import re
from pyspark.sql import Row
from ckonlpy.tag import Twitter, Postprocessor


# 입력 dataframe 생성
def make_df():
    PATH = './S07P22D106/data/testutf8.csv'

    # sqoop에서 온 데이터 + 컬럼명 추가하기
    schema = StructType([
        StructField("reviewIndex", LongType(), True),   # index: [0]
        StructField("memberIndex", LongType(), True),
        StructField("drinkIndex", LongType(), True),
        StructField("createdAt", DateType(), True),
        StructField("updatedAt", DateType(), True),
        StructField("weekday", StringType(), True),
        StructField("memberId", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("gender", StringType(), True),
        StructField("score", IntegerType(), True),
        StructField("review", StringType(), True),  # index: [10]
        StructField("isCrawled", IntegerType(), True)
    ])

    # 컬럼명 추가한 초기 데이터
    spark = SparkSession.builder\
        .master('local[*]')\
        .appName('SparkSQL')\
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    df = spark.read.csv(PATH, schema=schema)
    return df


# 형태소 분석기
def check_correct(text):
    twitter = Twitter()
    
    # customizing dictionary
    twitter.add_dictionary('막걸리인', 'Noun')
    # not use words
    stopwords = {'은', '는', '이', '가'}
    # passwords 에 등록된 단어, (단어, 품사)만 출력됩니다.
    # passwords = {'아이오아이', ('정말', 'Noun')}
    # postprocessor = Postprocessor(twitter, passwords = passwords)
    
    postprocessor = Postprocessor(twitter, stopwords=stopwords)
    text.replace("\n", " ").replace("\t", " ")     # 개행문자 제거
    pattern_punctuation = re.compile(r'[^\w\s]')    # 정규표현식(특수문자 제거)
    text = pattern_punctuation.sub('', text)
    result = postprocessor.pos(text)
    return result


# 모든 review 모으고 형태소 분석 및, word counting
def check_all_reviews(dataframe):
    # 모든 리뷰 합친 dataframe 만들기
    df = dataframe.agg(f.concat_ws(" ", f.collect_list(f.col("review"))).alias("reviews"))

    # 전체 리뷰를 형태소 분석하기
    checkedReview = check_correct(df.collect()[0][0])   
    # 새로운 dataframe 만들어서 형태소 분석한 결과 넣기
    data = [Row(checkedReview)]
    spark = SparkSession.builder.getOrCreate()
    df3 = spark.createDataFrame(data).toDF("review") \
        .withColumn('review', f.col('review').cast('string'))

    # [{}, {}, {}] 형태를 쪼개기
    df4 = df3.withColumn('word', f.explode(f.split(f.col('review'), ', '))) \
        .groupBy('word') \
        .count() \
        .sort('count', ascending=False)
        
    # "{", "}" 문자 없애기
    df5 = df4.withColumn("word", f.regexp_replace("word", "\\{|\\}", ""))
    return df5


def main():
    # dataframe 만들기
    df = make_df()
    
    # 모든 review(18만개)에 대해 형태소 문석 및 워드 카운팅
    all_df = check_all_reviews(df)
    all_df.write.csv('./csv')
    all_df.show()

    
if __name__ == "__main__":
    main()