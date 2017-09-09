<template>
    <div>
        <h1 class="text-center"  v-if="this.$store.getters.isAuthenticated">Welcome <b>{{ this.$store.getters.username }} </b>!</h1>
        <h1  class="text-center" v-if="!this.$store.getters.isAuthenticated">
            <router-link to="/login" activeClass="active" ><a>Log In</a></router-link>
        </h1>
    </div>

</template>