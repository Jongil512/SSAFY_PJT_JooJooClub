<template>
  <signout-form v-if="isCurrentUser" :currentUser="currentUser"></signout-form>
</template>

<script>
import { mapGetters } from 'vuex'
import SignoutForm from '@/components/accounts/SignoutForm.vue'
export default {
  name: 'SignOutView',
  components: {SignoutForm},
  computed: {
    ...mapGetters(['currentUser', 'isCurrentUser'])
  },
}
</script>

<style>
.sub-error {
  color: red;
}
</style>