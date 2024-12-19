/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './static/**/*.css',
    './templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
}

