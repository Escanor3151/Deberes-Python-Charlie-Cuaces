#Iteración de arreglos multidimensionales con bucles anidados - Charlie Cuaces
temperatura = [
    [#Ciudad 1 - Quito
        [   # Semana 1
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 27},
            {"dia": "Miércoles", "temp": 25},
            {"dia": "Jueves", "temp": 26},
            {"dia": "Viernes", "temp": 18},
            {"dia": "Sábado", "temp": 15},
            {"dia": "Domingo", "temp": 28}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 10},
            {"dia": "Martes", "temp": 12},
            {"dia": "Miércoles", "temp": 17},
            {"dia": "Jueves", "temp": 20},
            {"dia": "Viernes", "temp": 19},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 9},
            {"dia": "Martes", "temp": 7},
            {"dia": "Miércoles", "temp": 14},
            {"dia": "Jueves", "temp": 15},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 24},
            {"dia": "Domingo", "temp": 8}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 20},
            {"dia": "Martes", "temp": 21},
            {"dia": "Miércoles", "temp": 21},
            {"dia": "Jueves", "temp": 27},
            {"dia": "Viernes", "temp": 24},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 21}
        ]
    ],
    [#Ciudad 2 - Guayaquil
        [   # Semana 1
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 29},
            {"dia": "Viernes", "temp": 35},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 25},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 31},
            {"dia": "Viernes", "temp": 24},
            {"dia": "Sábado", "temp": 30},
            {"dia": "Domingo", "temp": 32}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 29},
            {"dia": "Viernes", "temp": 35},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 32}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 29},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 22}
        ]
    ],
    [#Ciudad 3 - Cuenca
        [   # Semana 1
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 10},
            {"dia": "Miércoles", "temp": 12},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 18},
            {"dia": "Martes", "temp": 20},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 22}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 17},
            {"dia": "Martes", "temp": 21},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 20},
            {"dia": "Viernes", "temp": 24},
            {"dia": "Sábado", "temp": 21},
            {"dia": "Domingo", "temp": 17}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 20},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 26},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 22}
        ]
    ]
]
for ciudad in temperatura:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma +=dia['temp']
            prom=suma/7
        print ("El promedio es: ",prom)