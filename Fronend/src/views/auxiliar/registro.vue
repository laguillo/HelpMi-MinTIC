<template>
    <menuAuxiliar></menuAuxiliar>

    <div class="mt-6 flex justify-center bg-white p-6 rounded shadow-sm">
        <form v-on:submit.prevent="processSignUp" id="formRegistro">
            <h2 class="font-bold text-xl text-center mt-2 mb-6 uppercase">Registro de nuevo usuario</h2>
            <div class="grid grid-cols-2 gap-6">
                <div>
                    <label for="username" class="block text-xs uppercase font-semibold">Usuario</label>
                    <input type="text" id="username"
                        class="mb-2 bg-gray-50 border border-gray-300 rounded focus:ring-helpmi-500 focus:border-helpmi-500 block p-1.5"
                        v-model="user.username" placeholder="Username" required>

                    <label for="password" class="block text-xs uppercase font-semibold">Contraseña</label>
                    <input type="password" id="password"
                        class="mb-2 bg-gray-50 border border-gray-300 rounded focus:ring-helpmi-500 focus:border-helpmi-500 block p-1.5"
                        v-model="user.password" placeholder="••••••••" required>

                    <label for="rol" class="block text-xs uppercase font-semibold">Rol</label>
                    <select id="rol" v-model="user.rol" required
                        class="mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded focus:ring-helpmi-500 focus:border-helpmi-500 block w-full p-1.5">
                        <option value="A">Auxiliar</option>
                        <option value="E">Enfermero</option>
                        <option value="M">Medico</option>
                        <option value="P">Paciente</option>
                        <option value="F">Familiar Paciente</option>
                    </select>

                    <label for="nombre" class="block text-xs uppercase font-semibold">Nombre</label>
                    <input type="text" id="nombre"
                        class="mb-2 bg-gray-50 border border-gray-300 rounded focus:ring-helpmi-500 focus:border-helpmi-500 block p-1.5"
                        v-model="user.nombre" placeholder="Nombre" required>

                    <label for="apellido" class="block text-xs uppercase font-semibold">Apellido</label>
                    <input type="text" id="apellido"
                        class="mb-2 bg-gray-50 border border-gray-300 rounded focus:ring-helpmi-500 focus:border-helpmi-500 block p-1.5"
                        v-model="user.apellido" placeholder="Apellido" required>
                </div>

                <div>
                    <label for="tipoDocumento" class="block text-xs uppercase font-semibold">Tipo de documento</label>
                    <select id="tipoDocumento" v-model="user.tipoDocumento" required
                        class="mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded focus:ring-helpmi-500 focus:border-helpmi-500 block w-full p-1.5">
                        <option value="CC">Cedula de Ciudadania</option>
                        <option value="RC">Registro Civil</option>
                        <option value="TI">Tarjeta de Identidad</option>
                    </select>

                    <label for="documento" class="block text-xs uppercase font-semibold">Número</label>
                    <input type="text" id="documento"
                        class="mb-2 bg-gray-50 border border-gray-300 rounded focus:ring-helpmi-500 focus:border-helpmi-500 block p-1.5"
                        v-model="user.documento" placeholder="Número de documento" required>

                    <label for="email" class="block text-xs uppercase font-semibold">Correo Electronico</label>
                    <input type="text" id="email"
                        class="mb-2 bg-gray-50 border border-gray-300 rounded focus:ring-helpmi-500 focus:border-helpmi-500 block p-1.5"
                        v-model="user.email" placeholder="correo@mail.com" required>

                    <label for="celular" class="block text-xs uppercase font-semibold">Celular</label>
                    <input type="text" id="celular"
                        class="mb-2 bg-gray-50 border border-gray-300 rounded focus:ring-helpmi-500 focus:border-helpmi-500 block p-1.5"
                        v-model="user.celular" placeholder="Número de Celular" required>

                    <label for="genero" class="block text-xs uppercase font-semibold">Genero</label>
                    <select id="genero" v-model="user.genero" required
                        class="mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded focus:ring-helpmi-500 focus:border-helpmi-500 block w-full p-1.5">
                        <option value="M">Masculino</option>
                        <option value="F">Femenino</option>
                    </select>
                </div>
            </div>
            
            <label for="direccion" class="block text-xs uppercase font-semibold">Dirección</label>
            <input type="text" id="direccion"
                class="mb-2 bg-gray-50 border border-gray-300 rounded focus:ring-helpmi-500 focus:border-helpmi-500 block p-1.5 w-full"
                v-model="user.direccion" placeholder="Dirección de residencia">

            <!-- <input type="number" v-model="user.account.balance" placeholder="Initial Balance"> -->
            <button class="py-2 px-4 font-medium bg-helpmi-500 text-white rounded w-full mt-2 text-base hover:bg-helpmi-600" type="submit">Registrar Usuario</button>
        </form>
    </div>
</template>

<script>
import menuAuxiliar from "@/components/auxiliar/menuComponent.vue";
import axios from 'axios';
export default {
    name: "SignUp",
    data: function () {
        return {
            user: {
                username: "",
                password: "",
                rol: "",
                nombre: "",
                apellido: "",
                tipoDocumento: "",
                documento: "",
                email: "",
                celular: "",
                direccion: "",
                genero: ""
            }
        }
    },
    methods: {
        processSignUp: function () {
            axios.post(
                "https://helpmi-be.herokuapp.com/user/",
                this.user,
                { headers: {} }
            )
                .then((result) => {
                    // let dataSignUp = {
                    //     username: this.user.username,
                    //     token_access: result.data.access,
                    //     token_refresh: result.data.refresh,
                    // }
                    this.$emit('completedSignUp')
                })
                .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en el registro.");
                });
        }
    },
    components: { menuAuxiliar }
}
</script>