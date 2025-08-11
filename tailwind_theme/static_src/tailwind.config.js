/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../../**/*.{html,py,js}",
    "./src/**/*.{html,js,css}"
  ],
  theme: {
    extend: {
      colors: {
        'deep-sea': {
          50: '#e0e1dd',
          100: '#d1d3ce',
          200: '#b3b7b0',
          300: '#959b92',
          400: '#778da9',
          500: '#5a7a8c',
          600: '#415a77',
          700: '#2a3a63',
          800: '#1b263b',
          900: '#0d1b2a',
        },
        'primary': {
          50: '#e0e1dd',
          100: '#d1d3ce',
          200: '#b3b7b0',
          300: '#959b92',
          400: '#778da9',
          500: '#5a7a8c',
          600: '#415a77',
          700: '#2a3a63',
          800: '#1b263b',
          900: '#0d1b2a',
        },
        'accent': {
          50: '#778da9',
          100: '#6a7f9b',
          200: '#5d728d',
          300: '#50657f',
          400: '#415a77',
          500: '#344f6f',
          600: '#274467',
          700: '#1a395f',
          800: '#0d2e57',
          900: '#00234f',
        }
      },
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.5s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: [
      {
        'deep-sea': {
          'primary': '#415a77',
          'secondary': '#778da9',
          'accent': '#e0e1dd',
          'neutral': '#1b263b',
          'base-100': '#0d1b2a',
          'base-200': '#1b263b',
          'base-300': '#415a77',
          'info': '#778da9',
          'success': '#e0e1dd',
          'warning': '#778da9',
          'error': '#e0e1dd',
        },
      },
    ],
  },
}
