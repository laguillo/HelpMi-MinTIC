import { createRouter, createWebHistory } from "vue-router";
import App from "../App.vue";
import LogIn from "../views/LogIn.vue";
import HomePaciente from "../views/Home.vue";
import AccountPaciente from "../views/Account.vue";
import AccountEditPaciente from "../views/AccountEdit.vue";
// Paciente
import RegistrarSVPaciente from "../views/paciente/RegistrarSV.vue";
import HistoriaClinicaPaciente from "../views/paciente/HistoriaClinica.vue";
// Auxiliar
import Registro from "../views/auxiliar/registro.vue";
// Medico
import historiaClinicaMedico from "../views/medico/historiaClinica.vue"
import listaPacientes from "../views/medico/listaPacientes.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "root",
      component: App,
    },
    {
      path: "/user/logIn",
      name: "logIn",
      component: LogIn,
    },
    {
      path: "/user/home",
      name: "home",
      component: HomePaciente,
    },
    {
      path: "/user/account",
      name: "account",
      component: AccountPaciente,
    },
    {
      path: "/user/AccountEdit",
      name: "AccountEdit",
      component: AccountEditPaciente,
    },
    // Paciente
    {
      path: "/user/RegistrarSV",
      name: "RegistrarSV",
      component: RegistrarSVPaciente,
    },
    {
      path: "/user/HistoriaClinica",
      name: "HistoriaClinica",
      component: HistoriaClinicaPaciente,
    },
    // Auxiliar
    {
      path: "/user/registro",
      name: "registro",
      component: Registro,
    },
    // Medico
    {
      path: "/user/hc",
      name: "hc",
      component: historiaClinicaMedico,
    },
    {
      path: "/user/listaPacientes",
      name: "listaPacientes",
      component: listaPacientes,
    },
  ],
});

export default router;
