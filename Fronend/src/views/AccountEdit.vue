<template>
    <menuPaciente v-if="rol === 'P'"></menuPaciente>
    <menuAuxiliar v-if="rol === 'A'"></menuAuxiliar>
    <menuMedico v-if="rol === 'M'"></menuMedico>
    <main class="flex gap-4 mt-6">
        <div class="shadow sm:rounded-lg w-3/4 bg-white">
            <h2 class="py-3 font-bold text-center bg-white border-b">Editar Perfil</h2>
            <div class="grid grid-cols-2 m-6 text-sm">
                
            </div>
        </div>
        <div v-if="rol === 'P'" class="shadow md:rounded-lg bg-white w-1/4">
            <h2 class="font-bold text-center py-3 border-b">Información Medica</h2>
            <div class="space-y-2 p-4 text-sm">
                <p class="font-semibold">Médico: <span class="font-normal">{{medico}}</span></p>
                <p class="font-semibold">Enfermero: <span class="font-normal">{{enfermero}}</span></p>
            </div>
        </div>
    </main>
</template>

<script>
import menuPaciente from "@/components/paciente/menuComponent.vue";
import menuAuxiliar from "@/components/auxiliar/menuComponent.vue";
import menuMedico from "@/components/medico/menuComponent.vue";
import jwt_decode from "jwt-decode";
import axios from "axios";
export default {
    name: "AccountEdit",
    data: function () {
        return {
            username: localStorage.getItem("username") || "none",
            nombre: "",
            apellido: "",
            documento: "",
            tipoDocumento: "",
            celular: "",
            email: "",
            direccion: "",
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
                this.$router.push({ name: "AccountEdit" });
        },
        getData: async function () {
            if (
                localStorage.getItem("token_access") === null ||
                localStorage.getItem("token_refresh") === null
            ) {
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
                    this.celular = result.data.celular;
                    this.email = result.data.email;
                    this.direccion = result.data.direccion;
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
                .post(
                    "https://helpmi-be.herokuapp.com/refresh/",
                    { refresh: localStorage.getItem("token_refresh") },
                    { headers: {} }
                )
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
    components: { menuPaciente, menuAuxiliar, menuMedico }
};
</script>
