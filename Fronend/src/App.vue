<template>
  <header class="py-4 flex items-center border-b">
    <img class="w-28" src="./assets/logo.svg" alt="">
    <nav class="ml-auto flex font-medium items-center space-x-4">
      <!-- <button class="py-2 px-4 font-semibold bg-helpmi-500 text-gray-50 rounded-full hover:bg-helpmi-600" v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button> -->
      <!-- <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button> -->
      <!-- <button v-if="is_auth" v-on:click="loadHome"> Inicio </button> -->
      <!-- <button class="py-2 px-4 font-semibold bg-helpmi-500 text-gray-50 rounded-full hover:bg-helpmi-600" v-if="is_auth" v-on:click="loadHome"><i class='bx bx-fw bx-user'></i>Mi Cuenta</button> -->
    </nav>
  </header>
  <div>
    <router-view v-on:completedLogIn="completedLogIn" v-on:completedSignUp="completedSignUp" v-on:logOut="logOut">
    </router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      is_auth: false
    }
  },

  components: {
  },

  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;
      if (this.is_auth == false)
        this.$router.push({ name: "logIn" });
      else
        this.$router.push({ name: "home" });
    },
    
    loadAccount: function () {
      this.$router.push({ name: "home" });
    },

    loadHome: function () {
      this.$router.push({ name: "home" });
    },

    logOut: function () {
      localStorage.clear();
      // alert("Sesión Cerrada");
      this.verifyAuth();
    },

    loadLogIn: function () {
      this.$router.push({ name: "logIn" })
    },

    loadSignUp: function () {
      this.$router.push({ name: "registro" })
    },

    completedLogIn: function (data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      this.verifyAuth();
    },

    completedSignUp: function (data) {
      alert("Registro Exitoso");
      const formregistro = document.getElementById("formRegistro")
      formregistro.reset();
      // this.completedLogIn(data);
    },
  },
  created: function () {
    this.verifyAuth()
  }
}
</script>
 