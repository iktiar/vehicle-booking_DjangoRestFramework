<template>
    <div class="col-sm-6 col-md-4">
        <div class="panel panel-success">
            <div class="panel-heading">
                <h3 class="panel-title">
                    Log In
                </h3>
            </div>
            <div class="panel-body">
                <div class="pull-left">
                    <input
                            type="text"
                            class="form-control"
                            placeholder="username"
                            v-model="username"
                            >
                    <input
                            type="password"
                            class="form-control"
                            placeholder="password"
                            v-model="password"
                            >
                </div>
                <div class="pull-right">
                    <button
                            class="btn btn-success"
                            @click="logIn"
                            >LogIn
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .danger {
        border: 1px solid red;
    }
</style>

<script>
export default {
    data () {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        logIn () {
            const userinfo = {
                username: this.username,
                password: this.password
            }
            this.$http.post('api-token-auth/', userinfo).then(response => {
                return response.json()
            })
            .then(data => {
                if (data.messages.token) {
                    this.getUserData(data.messages.token)
                    this.$store.dispatch('setToken', data.messages.token)
                }
            })
        },
        getUserData (token) {
            var config = { headers: {
                'Authorization': 'JWT ' + token
            }
            }
            this.$http.get('api/getuser/?username=' + this.username, config).then(response => {
                return response.json()
            }).then(data => {
                console.log(data.messages[0]['is_superuser'])
                this.$store.dispatch('setUserRole', data.messages[0]['is_superuser'])
                this.$router.push('/')
            })
        }
    },
    created () {
        if (this.$store.getters.isAuthenticated) {
            this.$router.push('/')
        }
    }
}
</script>