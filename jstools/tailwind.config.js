const colors = require('tailwindcss/colors')

module.exports = {
    purge: {
        mode: 'layers',
        content: [
            '../**/*.{js, jsx, ts, tsx}',
            '../templates/*.html',
            '../templates/**/*.html',
            '../**/templates/*.html',
            '../**/templates/**/*.html',
        ]
    },
    darkMode: 'class', // false or 'media' or 'class'
    theme: {
        fontFamily: {
            'acumin-pro-semi-condensed': ['acumin-pro-semi-condensed', 'sans-serif'],
            'acumin-pro-wide': ['acumin-pro-wide', 'sans-serif'],
        },
        extend: {
            colors: {
                'primary': colors.sky,
                'secondary': colors.blueGray,
                'cyan': colors.cyan,
                'sky': colors.sky,
                'lime': colors.lime,
                'true-gray': colors.trueGray,
                'warm-gray': colors.warmGray,
            },
        },
    },
    variants: {
        extend: {
            animation: ['hover', 'focus'],
            backgroundColor: ['active', 'checked'],
            borderColor: ['checked'],
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
}
