<template>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <div class="navbar-header">
                <router-link to="/" class="navbar-brand">Vehicle Booking</router-link>
            </div>

            <div class="collapse navbar-collapse">

                <ul  v-if="this.$store.getters.isAuthenticated" class="nav navbar-nav">
                    <router-link to="/requisition-ticket-form" activeClass="active" tag="li"><a>New Requisition</a></router-link>
                </ul>
                <ul  v-if="this.$store.getters.isSuperUser" class="nav navbar-nav">
                    <router-link to="/admin/requisition-tickets" activeClass="active" tag="li"><a>All Requisition</a></router-link>
                    <router-link to="/admin/reports" activeClass="active" tag="li"><a>All Reports</a></router-link>
                </ul>

                <transition>
                <strong v-if="this.$store.getters.isAuthenticated" class="navbar-text navbar-right">
                    <router-link to="#" v-on:click.native="logOut" activeClass="active" ><a>Log Out</a></router-link>
                </strong>
                <strong v-if="!this.$store.getters.isAuthenticated" class="navbar-text navbar-right">

                        <router-link to="/login" activeClass="active" ><a>Log In</a></router-link>
                    </strong>
                </transition>
                <!--
                <ul  v-if="this.$store.getters.isAuthenticated" class="nav navbar-nav navbar-right">
                    <li><a href="#" >End Day</a></li>
                    <li
                            class="dropdown"
                            :class="{open: isDropdownOpen}"
                            @click="isDropdownOpen = !isDropdownOpen">
                        <a
                                href="#"
                                class="dropdown-toggle"
                                data-toggle="dropdown"
                                role="button"
                                aria-haspopup="true"
                                aria-expanded="false">Save & Load <span class="caret"></span></a>

                    </li>
                </ul> -->
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>
</template>

<script>

export default {
    data () {
        return {
            isDropdownOpen: false,
            isSuperUser: false,
            userName: false
        }
    },
    methods: {
        logOut () {
            this.$store.dispatch('clearToken')
            this.$router.push('/logIn')
        }
    },
    created () {
        return this.$store.getters.isAuthenticated
    }
}
</script>