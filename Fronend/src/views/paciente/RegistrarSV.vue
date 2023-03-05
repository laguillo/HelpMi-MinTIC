<template>
    <menuPaciente></menuPaciente>
    <main class="flex gap-4 mt-6">
        <!-- Tabla Ultimos registros -->
        <div class="overflow-x-auto relative shadow sm:rounded-lg w-3/4">
            <h2 class="py-3 font-bold text-center bg-white border-b">Registrar Signos Vitales</h2>
            <form class="bg-white p-4">
                <label for="oximetria" class="block mb-1 text-xs uppercase font-semibold">Oximetría</label>
                <input
                    class="bg-gray-50 mb-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-helpmi-500 focus:border-helpmi-500 block w-25 p-2"
                    id="oximetria" type="number" placeholder="Oximatría">
                <label for="frecuenciaRespiratoria" class="block mb-1 text-xs uppercase font-semibold">Frecuencia
                    Respiratoria</label>
                <input
                    class="bg-gray-50 mb-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-helpmi-500 focus:border-helpmi-500 block w-25 p-2"
                    id="frecuenciaRespiratoria" type="number" placeholder="Frecuencia Respiratoria">
                <label for="frecuenciaCardiaca" class="block mb-1 text-xs uppercase font-semibold">Frecuencia
                    Cardíaca</label>
                <input
                    class="bg-gray-50 mb-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-helpmi-500 focus:border-helpmi-500 block w-25 p-2"
                    id="frecuenciaCardiaca" type="number" placeholder="Frecuencia Cardíaca">
                <label for="temperatura" class="block mb-1 text-xs uppercase font-semibold">Temperatura</label>
                <input
                    class="bg-gray-50 mb-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-helpmi-500 focus:border-helpmi-500 block w-25 p-2"
                    id="temperatura" type="number" placeholder="Temperatura">
                <label for="presionArterial" class="block mb-1 text-xs uppercase font-semibold">Presión Arterial</label>
                <input
                    class="bg-gray-50 mb-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-helpmi-500 focus:border-helpmi-500 block w-25 p-2"
                    id="presionArterial" type="number" placeholder="Presión Arterial">
                <label for="glicemia" class="block mb-1 text-xs uppercase font-semibold">Glicemia</label>
                <input
                    class="bg-gray-50 mb-2 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-helpmi-500 focus:border-helpmi-500 block w-25 p-2"
                    id="glicemia" type="number" placeholder="Glicemia">
                <button class="bg-helpmi-500 py-2 px-4 rounded-full text-white mt-4 hover:bg-helpmi-600" type="submit">Registrar Signos Vitales</button>
            </form>
        </div>
        <div class="shadow md:rounded-lg bg-white w-1/4">
            <h2 class="font-bold text-center py-3 border-b">Información Medica</h2>
            <div class="space-y-2 p-4 text-sm">
                <p class="font-semibold">Médico: <span class="font-normal">David López</span></p>
                <p class="font-semibold">Enfermero: <span class="font-normal">Jorge Mendoza</span></p>
            </div>
        </div>
    </main>
</template>

<script>
import menuPaciente from '@/components/paciente/menuComponent.vue';
import jwt_decode from "jwt-decode";
import axios from "axios";
export default {
    name: "RegistrarSV",
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
                this.$router.push({ name: "RegistrarSV" });
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
    components: { menuPaciente }
};
</script>
