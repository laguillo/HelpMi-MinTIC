/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
      },
      colors: {
        helpmi: {
          50: "#E5FAFF",
          100: "#C7F5FF",
          200: "#80E8FF",
          300: "#1AD5FF",
          400: "#00B7E0",
          500: "#0095B6",
          600: "#0085A3",
          700: "#00758F",
          800: "#006075",
          900: "#004757",
        },
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
