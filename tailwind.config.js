/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.html',
  "./node_modules/flowbite/**/*.js"
],
  
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/forms'),
    require('flowbite/plugin'),
  ],
}
