<template>
  <div class="container">
    <app-header></app-header>
    <div class="row">
        <div class="col-xs-12">
            <router-view></router-view>
            <!--  <CompletedTodos></CompletedTodos>
            <GetTodo></GetTodo>
            <CurrentTodos></CurrentTodos> -->
        </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header'
import GetTodo from './components/todo/GetTodo.vue'
import CurrentTodos from './components/todo/CurrentTodos.vue'
import CompletedTodos from './components/todo/CompletedTodos.vue'

export default {
    components: {
        appHeader: Header,
        GetTodo,
        CurrentTodos,
        CompletedTodos

    },
    created () {
        const token = localStorage.getItem('token')

        if (token) {
            this.$store.dispatch('setToken', token)
        }
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
