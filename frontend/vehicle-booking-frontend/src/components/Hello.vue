<template>
  <div class="hello">
    <h1>{{ users }} {{ node }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
      <li><a href="https://gitter.im/vuejs/vue" target="_blank">Gitter Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
      <br>
      <li><a href="http://vuejs-templates.github.io/webpack/" target="_blank">Docs for This Template</a></li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">vue-router</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">vuex</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul>
    <br><br>
    <button class="btn btn-primary" @click="fetchData">Get Data</button>
    <br><br>
    <ul class="list-group">
      <li class="list-group-item" v-for="u in users.messages">{{ u.requisitionTicketLog_id }} - {{ u.type }} - {{ u.from_date_time}} - {{ u.to_date_time}}</li>
    </ul>
  </div>

</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      user: {
        requisitionTicketLog_id: '',
        type: ''
      },
      users: [],
      resource: {},
      node: 'data',
      msg: 'Welcome to Your Vue.js App, Iktiar!'
    }
  },
  methods: {
    fetchData () {
      this.$http.get('api/requisitionticket/')
        .then(response => {
          return response.json()
        })
        .then(data => {
          console.log(data)
          this.users = data
        })
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
