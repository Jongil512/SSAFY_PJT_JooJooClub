<template>
  <div class="container">
    <footer class="row row-cols-1 row-cols-sm-2 row-cols-md-5 py-5 my-5 border-top">
      <div class="d-flex justify-content-center footerImgWrap col mb-3">
        <img class="footerImg d-flex align-items-center mb-3 link-dark text-decoration-none bi" src="@/assets/logo_for_footer.png" alt="joojooclub">
      </div>

      <div class="col mb-3">
      </div>

      <div class="footerCenter col mb-5">
        <p class="title">Community</p>
        <ul class="nav flex-column">
          <li class="nav-item mb-2"><div @click="openInNewTab('https://www.notion.so/2-e109b4c80a8d4fddaec3810e9735adb3')" class="nav-link p-0 text-muted open-link">NOTION</div></li>
          <li class="nav-item mb-2"><div @click="openInNewTab('https://lab.ssafy.com/s07-bigdata-dist-sub2/S07P22D106')" class="nav-link p-0 text-muted open-link">GITLAB</div></li>
        </ul>
      </div>
      <div class="footerCenter col mb-5">
        <p class="title">Developers</p>
        <p class="info open-link" @click="openInNewTab('https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp')">Samsung SW Academy For Youth</p>
        <p class="info">정종일, 김민정, 박지은, 오도석, 최연지</p>
      </div>
      <div class="footerRight col mb-3">
        <p class="title text-muted">Copyright @ 2022 by D106</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'FooterCom',
  methods: {
    openInNewTab(url) {
      const win = window.open(url, '_blank')
      win.focus();
    }
  },
}
</script>

<style scoped>
  
  * {
	font-family: 'NanumSquareRound';
}

  :hover.open-link {
    cursor: pointer;
  }

  .footerImg {
    min-height: 90px;
    max-height: 110px;
    height: 12vh;
    margin: 0;
  }

  .footer {
    margin: 100px 0px 0px 0px;
    padding-bottom: 50px;
  }

  .footerCenter {
    margin-bottom: 20vh;
  }

  .title {
    font-weight: bold;
  }

  .link {
    font-size: smaller;
  }

  .info {
    font-size: smaller;
  }

  a { color: rgb(0, 0, 0); }
  a:visited { color: rgb(0, 0, 0); }
  a:hover { color: rgb(0, 0, 0); }
  a:active { color: rgb(0, 0, 0); }
</style>