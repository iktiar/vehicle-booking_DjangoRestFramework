import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        todos: [],
        newTodo: '',
        token: null,
        isSuperUser: null,
        username: null
    },
    mutations: {
        GET_TODO (state, todo) {
            state.newTodo = todo
        },
        ADD_TODO (state) {
            state.todos.push({
                body: state.newTodo,
                completed: false
            })
        },
        EDIT_TODO (state, todo) {
            var todos = state.todos
            todos.splice(todos.indexOf(todo), 1)
            state.todos = todos
            state.newTodo = todo.body
        },
        REMOVE_TODO (state, todo) {
            var todos = state.todos
            todos.splice(todos.indexOf(todo), 1)
        },
        COMPLETE_TODO (state, todo) {
            todo.completed = !todo.completed
        },
        CLEAR_TODO (state) {
            state.newTodo = ''
        },
        SET_TOKEN (state, token) {
            state.token = token
            localStorage.setItem('token', token)
        },
        CLEAR_TOKEN (state) {
            state.token = null
            localStorage.removeItem('token')
        },
        SET_USER_ROLE (state, rolestatus) {
            state.isSuperUser = rolestatus
        },
        SET_USER_NAME (state, username) {
            console.log(username)
            state.username = username
        }

    },
    actions: {
        getTodo ({commit}, todo) {
            commit('GET_TODO', todo)
        },
        addTodo ({commit}) {
            commit('ADD_TODO')
        },
        editTodo ({commit}, todo) {
            commit('EDIT_TODO', todo)
        },
        removeTodo ({commit}, todo) {
            commit('REMOVE_TODO', todo)
        },
        completeTodo ({commit}, todo) {
            commit('COMPLETE_TODO', todo)
        },
        clearTodo ({commit}) {
            commit('CLEAR_TODO')
        },
        setToken ({commit}, token) {
            commit('SET_TOKEN', token)
        },
        clearToken ({commit}) {
            commit('CLEAR_TOKEN')
        },
        setUserRole ({commit}, rolestatus) {
            commit('SET_USER_ROLE', rolestatus)
        },
        setUserName ({commit}, username) {
            console.log('store setUserName ..' + username)
            commit('SET_USER_NAME', username)
        }
    },
    getters: {
        newTodo: state => state.newTodo,
        todos: state => state.todos.filter((todo) => { return !todo.completed }),
        completedTodos: state => state.todos.filter((todo) => { return todo.completed }),
        isAuthenticated (state) {
            return state.token != null
        },
        token: state => state.token,
        isSuperUser: state => state.isSuperUser,
        username: state => state.username
    }

})
