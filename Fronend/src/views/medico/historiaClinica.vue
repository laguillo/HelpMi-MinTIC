<template>
    <menuMedico></menuMedico>
    <!-- Paciente -->
    <main class="flex gap-4 mt-6">
        <!-- Tabla Ultimos registros -->
        <div class="overflow-x-auto relative shadow sm:rounded-lg w-full">
            <h2 class="py-3 font-bold text-center bg-white border-b">Ultimos Registros</h2>
            <table class="w-full text-sm mt-2 text-center">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                    <tr>
                        <th scope="col" class="py-3 px-6">
                            Fecha
                        </th>
                        <th scope="col" class="py-3 px-6">
                            Realizador Por:
                        </th>
                        <th scope="col" class="py-3 px-6">
                            Acción
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-white border-b hover:bg-gray-50">
                        <th scope="row" class="py-4 px-6 font-medium whitespace-nowrap">
                            02/10/2022
                        </th>
                        <td class="py-4 px-6">
                            Paciente
                        </td>
                        <td class="py-4 px-6">
                            <a href="#" class="font-medium text-helpmi-600 hover:underline">Ver Informe</a>
                        </td>
                    </tr>
                    <tr class="bg-white border-b hover:bg-gray-50">
                        <th scope="row" class="py-4 px-6 font-medium whitespace-nowrap">
                            30/09/2022
                        </th>
                        <td class="py-4 px-6">
                            Paciente
                        </td>
                        <td class="py-4 px-6">
                            <a href="#" class="font-medium text-helpmi-600 hover:underline">Ver Informe</a>
                        </td>
                    </tr>
                    <tr class="bg-white hover:bg-gray-50">
                        <th scope="row" class="py-4 px-6 font-medium whitespace-nowrap">
                            29/09/2022
                        </th>
                        <td class="py-4 px-6">
                            Familiar
                        </td>
                        <td class="py-4 px-6">
                            <a href="#" class="font-medium text-helpmi-600 hover:underline">Ver Informe</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </main>
</template>

<script>
import menuMedico from "@/components/medico/menuComponent.vue";
import jwt_decode from "jwt-decode";
import axios from "axios";
export default {
    name: "Home",
    data: function () {
        return {
            username: localStorage.getItem("username") || "none",
            nombre: "",
            apellido: "",
            documento: "",
            tipoDocumento: "",
            genero: "",
            rol: "",
            medico: "",
            enfermero: "",
            loaded: false,
        };
    },
    methods: {
        verifyAuth: function () {
            this.is_auth = localStorage.getItem("isAuth") || false;
            if (this.is_auth == false)
                this.$router.push({ name: "logIn" });
            else
                this.$router.push({ name: "home" });
        },
        getData: async function () {
            if (localStorage.getItem("token_access") === null ||
                localStorage.getItem("token_refresh") === null) {
                this.$emit("logOut");
                return;
            }
            await this.verifyToken();
            let token = localStorage.getItem("token_access");
            let userId = jwt_decode(token).user_id.toString();
            axios
                .get(`https://helpmi-be.herokuapp.com/user/${userId}/`, {
                headers: { Authorization: `Bearer ${token}` },
            })
                .then((result) => {
                this.nombre = result.data.nombre;
                this.apellido = result.data.apellido;
                this.documento = result.data.documento;
                this.tipoDocumento = result.data.tipoDocumento;
                this.genero = result.data.genero;
                this.rol = result.data.rol;
                this.medico = result.data.medico;
                this.enfermero = result.data.enfermero;
                // this.balance = result.data.account.balance;
                this.loaded = true;
            })
                .catch(() => {
                this.$emit("logOut");
            });
        },
        verifyToken: function () {
            return axios
                .post("https://helpmi-be.herokuapp.com/refresh/", { refresh: localStorage.getItem("token_refresh") }, { headers: {} })
                .then((result) => {
                localStorage.setItem("token_access", result.data.access);
            })
                .catch(() => {
                this.$emit("logOut");
            });
        },
    },
    created: async function () {
        this.getData();
    },
    components: { menuMedico }
};
</script>
