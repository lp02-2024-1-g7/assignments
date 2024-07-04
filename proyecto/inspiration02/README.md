# Proyecto de Sistema de Actores en Go

Este proyecto implementa un sistema básico de actores en Go, donde dos actores se comunican entre sí utilizando TCP. Cada actor puede ser configurado a través de argumentos de línea de comandos.

## Estructura del Proyecto

El proyecto consta de un solo archivo:

- `actor.go`: Contiene la implementación del sistema de actores.

## Requisitos

- Go instalado en tu máquina. Puedes descargarlo desde [golang.org](https://golang.org/).

## Compilación y Ejecución

### Paso 1: Compilar el código

```bash
go build -o actor actor.go
```

### Paso 2: Ejecutar los actores

Debes abrir dos terminales separadas para ejecutar los dos actores.

#### Terminal 1: Ejecutar Actor 1

```bash
./actor 1 :6000
```

#### Terminal 2: Ejecutar Actor 2

```bash
./actor 2 :6001
```

### Comunicación entre Actores

- El Actor 1 enviará un mensaje al Actor 2 después de un breve retraso.
- Ambos actores estarán escuchando en sus respectivos puertos para recibir mensajes.

### Uso de Argumentos de Línea de Comandos

El programa `actor.go` toma dos argumentos:

1. **actor_id**: Un identificador único para el actor (en este caso, `1` o `2`).
2. **port**: El puerto en el que el actor estará escuchando (por ejemplo, `:6000` o `:6001`).

Ejemplo de ejecución:

```bash
./actor <actor_id> <port>
```

