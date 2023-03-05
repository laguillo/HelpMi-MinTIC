<template>
    <section class="">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-[calc(100vh-200px)] lg:py-0">
            <div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl">
                        Iniciar Sesión
                    </h1>
                    <form v-on:submit.prevent="processLogInUser" class="space-y-4 md:space-y-6">
                        <div>
                            <label for="usuraio" class="block mb-2 text-sm font-medium text-gray-900">Usuario</label>
                            <input v-model="user.username" type="text" name="email" id="usuario"
                                class="border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-helpmi-600 focus:border-helpmi-600 block w-full p-2.5"
                                placeholder="Nombre de usuario" required="" />
                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900">Contraseña</label>
                            <input v-model="user.password" type="password" name="password" id="password"
                                placeholder="••••••••"
                                class="border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-helpmi-600 focus:border-helpmi-600 block w-full p-2.5"
                                required="" />
                        </div>
                        <!-- <div class="flex items-center justify-between">
                            <div class="flex items-start">
                                <div class="flex items-center h-5">
                                    <input id="remember" type="checkbox"
                                        class="w-4 h-4 border border-gray-300 rounded focus:ring-3 focus:ring-helpmi-300" />
                                </div>
                                <div class="ml-3 text-sm">
                                    <label for="remember" class="text-gray-500">Recordarme</label>
                                </div>
                            </div>
                            <a href="#" class="text-sm font-medium text-helpmi-600 hover:underline">Olvide mi
                                contraseña</a>
                        </div> -->
                        <button type="submit"
                            class="w-full text-white bg-helpmi-600 hover:bg-helpmi-700 focus:ring-4 focus:outline-none focus:ring-helpmi-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">
                            Entrar
                        </button>
    
                        <!-- <p class="text-sm font-light text-gray-500">
                            Aún no tienes cuenta?
                            <a href="#" class="font-medium text-helpmi-600 hover:underline">Solicitar Registro</a>
                        </p> -->
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';
export default {
    name: "LogIn",
    data: function () {
        return {
            user: {
                username: "",
                password: ""
            }
        }
    },
    methods: {
        processLogInUser: function () {
            axios.post(
                "https://helpmi-be.herokuapp.com/login/",
                this.user,
                { headers: {} }
            )
                .then((result) => {
                    let dataLogIn = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    this.$emit('completedLogIn', dataLogIn)
                })
                .catch((error) => {
                    if (error.response.status == "401")
                        alert("Credenciales Incorrectas.");
                });
        }
    }
}
</script>