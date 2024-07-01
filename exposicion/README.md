# Script de Exposición grupo 7, Actores: Capitulo 4 del libro “Programming Distributed Computing Systems" (PDCS) del profesor Carlos A. Varela.

### Diapositivas en Canva
* https://www.canva.com/design/DAF_K5aOdkU/nrGkJVDPAOFQW2V1Y-o8Zw/edit


### **Diapositiva 1: Introducción (Fredy)**

"Buenos días/tardes a todos. Gracias por acompañarnos en esta presentación donde exploraremos el modelo de actores, un paradigma revolucionario en la computación concurrente y en sistemas distribuidos. Este modelo, introducido en los años 70 por Carl Hewitt, ha ido evolucionando para convertirse en una pieza angular en el diseño de sistemas robustos y eficientes, especialmente en entornos distribuidos donde la comunicación asíncrona y la gestión eficaz de estados son críticos.

El modelo de actores redefine la manera en que pensamos sobre la ejecución concurrente, ofreciendo un marco donde cada actor opera como una entidad independiente, capaz de procesar información, comunicarse, y crear nuevos actores de manera asincrónica. Esta capacidad para gestionar la concurrencia sin los problemas habituales asociados con los bloqueos y la sincronización de estados, hace del modelo de actores una herramienta poderosa en el diseño de sistemas complejos.

Durante nuestra presentación, cubriremos desde las bases teóricas que sustentan el modelo de actores, pasando por su implementación práctica, hasta llegar a discutir casos de uso reales que demuestran su aplicabilidad y eficacia. Esperamos que al final de esta charla, tengan una comprensión clara de cómo el modelo de actores puede transformar el desarrollo de software, especialmente en áreas que requieren alta concurrencia y distribución."

### **Diapositiva 2: Agenda (Juan)**

"Para guiar nuestro viaje a través del modelo de actores, hemos estructurado nuestra presentación en varias secciones clave. Comenzaremos estableciendo las bases teóricas, conceptos esenciales y la filosofía que fundamentan el modelo de actores.

Después, profundizaremos en el modelo conceptual de actores, explorando las propiedades y características que los definen. Discutiremos cómo los actores se comunican, gestionan su estado y cómo la creación dinámica de actores facilita la escalabilidad y la adaptabilidad de los sistemas.

En la implementación veremos cómo se traduce la teoría a la práctica. A través de ejemplos concretos, con el lenguaje de programación Golang, ilustraremos cómo se pueden construir actores, enviar y recibir mensajes, y cómo gestionar la concurrencia.

Veremos casos de uso reales del modelo de actores para comprender mejor su aplicabilidad y las ventajas que ofrece en casos que van, desde sistemas de telecomunicaciones hasta aplicaciones web de alta carga.

Concluirémos nuestra exposición con una sección de conclusiones, donde resumiremos los puntos clave discutidos y reflexionaremos sobre las ventajas y desventajas del modelo de actores.

### **Diapositiva 3: Bases Teóricas (Fredy)**

"Adentrándonos en las bases teóricas del modelo de actores, es esencial reconocer que este paradigma fue concebido como una solución a los desafíos inherentes a la computación concurrente y distribuida. Los sistemas distr ibuidos abiertos, caracterizados por su capacidad para incorporar cambios dinámicos, la adición de nuevos componentes y la sustitución de los existentes, requieren un marco de trabajo flexible y robusto para su gestión eficiente.

El modelo de actores responde a estos retos mediante la introducción de una abstracción simple pero poderosa: un actor. Los actores son entidades autónomas que encapsulan estado y comportamiento, comunicándose exclusivamente a través del intercambio de mensajes. Esta comunicación asincrónica permite que los actores operen de manera concurrente sin compartir estado, eliminando así muchos de los problemas asociados con los bloqueos y las condiciones de carrera típicos de otros modelos de concurrencia.

Además, el modelo de actores introduce conceptos de creación dinámica de actores y de justa distribución de mensajes, asegurando que cada mensaje enviado sea eventualmente recibido y procesado. Este enfoque no solo mejora la robustez y la escalabilidad de los sistemas, sino que también ofrece una mayor tolerancia a fallos, ya que el aislamiento entre actores significa que un error en un actor no se propaga automáticamente a otros.

La elegancia del modelo de actores radica en su simplicidad y en su poder para abstraer la complejidad inherente a la gestión de sistemas concurrentes y distribuidos. Al proporcionar un marco donde la comunicación, el procesamiento, y la creación de actores se manejan de manera transparente, el modelo permite a los desarrolladores centrarse en la lógica de aplicación en lugar de en los detalles de bajo nivel de la concurrencia y la distribución."

### **Diapositiva 4: Sistemas Distribuidos Abiertos (Juan)**

"Los sistemas distribuidos abiertos se caracterizan por su capacidad para adaptarse y evolucionar en entornos dinámicos. Fundamentalmente, deben permitir tres operaciones esenciales: cambios dinámicos en las conexiones entre componentes, adición de nuevos componentes y reemplazo de componentes existentes. Esta flexibilidad es crucial para mantener la eficacia de los sistemas a medida que evolucionan sus requisitos y su entorno operativo.

Cada actor en el sistema opera de manera independiente pero puede comunicarse con otros actores de manera asincrónica para realizar tareas complejas. Esta independencia y capacidad de comunicación ofrece una gran tolerancia a fallos, escalabilidad y adaptabilidad.

Consideremos, por ejemplo, un sistema de procesamiento de transacciones en línea que debe escalar dinámicamente para manejar variaciones en la carga de trabajo. Mediante el modelo de actores, se pueden agregar dinámicamente nuevos actores (o servicios) para manejar el aumento de transacciones sin interrumpir el servicio. Del mismo modo, si un componente falla, su actor correspondiente puede ser reemplazado o recuperado sin afectar el funcionamiento general del sistema.

### **Diapositiva 5: Modelo de Actores - Principios Fundamentales (Fredy)**

"Al adentrarnos en el corazón del modelo de actores, es esencial comprender sus principios fundamentales, que lo distinguen como un paradigma poderoso para la computación concurrente y distribuida. Este modelo, basado en la simplicidad y la eficiencia, se centra en los actores como las unidades básicas de ejecución. Cada actor es una entidad independiente con su propio estado, que interactúa exclusivamente mediante el envío y la recepción de mensajes asincrónicos. Esta naturaleza asincrónica es clave, permitiendo a los actores operar de manera concurrente sin bloqueos directos, lo que facilita la creación de sistemas más robustos y escalables.

El modelo de actores se apoya en tres acciones fundamentales que todo actor puede realizar:

1. **Enviar un mensaje** a otro actor conocido. Este mecanismo de comunicación subraya la naturaleza descentralizada y colaborativa del modelo, donde la transferencia de información y tareas se realiza sin compartir memoria o estado, eliminando así las condiciones de carrera y los bloqueos.
2. **Crear un nuevo actor**, lo que permite al sistema adaptarse y escalar dinámicamente. La capacidad de generar nuevos actores en tiempo de ejecución es fundamental para sistemas que necesitan ajustar su capacidad de procesamiento o funcionalidad en respuesta a la demanda o fallos.
3. **Decidir qué hacer al recibir un mensaje**, lo que incluye actualizar su propio estado o tomar acciones específicas. Esta decisión es crítica, ya que define el comportamiento del actor y cómo responde a diferentes situaciones, permitiendo una amplia gama de comportamientos y interacciones complejas entre actores.

Cada uno de estos principios contribuye a la flexibilidad y potencia del modelo de actores, ofreciendo un marco conceptual que es simultáneamente simple en su concepción pero capaz de modelar sistemas complejos y dinámicos. Al integrar estos principios, los desarrolladores pueden construir sistemas que son inherentemente paralelos y distribuidos, proporcionando soluciones efectivas a problemas de concurrencia y distribución que han plagado a los sistemas informáticos tradicionales.

### **Diapositiva 6: Actores como Unidad Fundamental de Computación (Juan)**

"Los actores encapsulan tres aspectos clave: procesamiento, almacenamiento de estado y comunicación. Esta encapsulación les permite, gestionar su propio estado interno y comunicrese con otros actores exclusivamente a través del intercambio de mensajes.

A diferencia de los modelos tradicionales que dependen de hilos y bloqueos para gestionar el acceso concurrente a recursos compartidos, los actores evitan estos problemas al no compartir estado. Cada actor procesa mensajes de manera secuencial, lo que garantiza que su estado interno solo sea modificado por un proceso a la vez, eliminando la necesidad de mecanismos de sincronización complejos.

Esto hace que el modelo sea inherentemente seguro en términos de concurrencia, hace que los mensajes pueden ser enviados entre actores que residen en diferentes nodos de una red, sin cambiar la naturaleza fundamental delos actores. Si un actor falla, solo afecta a ese actor y posiblemente a los que dependen directamente de él, permitiendo que el sistema se recupere o se reconfigure de manera más eficaz.

### **Diapositiva 7-8: Sintaxis del Lenguaje de Actores y Ejemplos (Fredy)**

"Ahora que comprendemos la importancia de los actores como unidades fundamentales de computación, es esencial explorar cómo se representan y se utilizan en la práctica. La sintaxis del lenguaje de actores varía según el framework o lenguaje de programación específico, pero existen conceptos comunes que permiten a los desarrolladores definir actores, especificar sus comportamientos y manejar mensajes.

Por ejemplo, en el lenguaje de programación Erlang, conocido por su robusto soporte para concurrencia y sistemas distribuidos, los actores son representados como procesos ligeros que intercambian mensajes. La creación de un actor (o proceso) se realiza mediante la llamada a una función que define su comportamiento, y la comunicación se maneja a través del envío de mensajes asincrónicos.

Un ejemplo simple podría ser un actor 'contador' que incrementa un contador interno cada vez que recibe un mensaje 'incrementar'. La definición de este actor incluiría la lógica para manejar el mensaje 'incrementar' y actualizar el estado interno del contador. Este ejemplo ilustra cómo los actores pueden encapsular estado y comportamiento, y cómo la comunicación asincrónica dirige la interacción entre actores.

Otro ejemplo es el uso del modelo de actores en Akka, un toolkit para la construcción de aplicaciones concurrentes y distribuidas en Java y Scala. Akka proporciona una API rica para definir actores, enviar mensajes y gestionar el ciclo de vida de los actores. Los desarrolladores pueden definir actores extendiendo una clase de actor base y sobrescribiendo un método para manejar mensajes entrantes. Este enfoque orientado a objetos facilita la organización del código y la definición de comportamientos complejos.

Estos ejemplos destacan cómo la sintaxis y las abstracciones proporcionadas por diferentes lenguajes y frameworks facilitan la implementación del modelo de actores. Al abstraer los detalles de la programación concurrente y distribuida, estos lenguajes permiten a los desarrolladores centrarse en la lógica de la aplicación, mejorando la claridad del código y reduciendo la probabilidad de errores."

### **Diapositiva 9: Representación Visual de Actores (Juan)**

"Para visualizar cómo interactúan los actores en un sistema Imaginaremos cada actor como un círculo o nodo dentro de una red. Cada nodo está conectado a otros a través de líneas que representan los mensajes enviados entre actores.

Visualmente, esto puede parecer un grafo dirigido, donde los nodos (actores) no tienen una jerarquía fija, lo que permite mucha flexibilidad.

La visualización ayuda a identificar patrones de comunicación, puntos de congestión potenciales y oportunidades para optimizar o escalar el sistema. Por ende, la representación visual es una herramienta poderosa tanto para el diseño como para el análisis de sistemas basados en el modelo de actores."

### **Diapositiva 10: Semánticas Operacionales (Fredy)**

"Adentrándonos en las semánticas operacionales del modelo de actores, exploramos los principios que rigen el comportamiento y la interacción de los actores. Las semánticas operacionales describen cómo los actores procesan mensajes, cómo pueden cambiar su comportamiento en respuesta a los mensajes recibidos y cómo estos principios garantizan la integridad y la consistencia del sistema.

Una propiedad fundamental es la no-preempción de los actores: un actor procesa un mensaje a la vez, lo que garantiza que su estado interno se mantenga coherente y predecible. Esto elimina la necesidad de bloqueos explícitos para acceso a recursos compartidos, reduciendo la complejidad y aumentando la eficiencia.

Otra característica clave es la entrega de mensajes. Aunque el modelo de actores asume una comunicación asincrónica, se espera que los mensajes enviados a un actor sean eventualmente entregados. Sin embargo, el modelo no garantiza un orden específico de entrega, lo que implica que los actores deben ser diseñados para manejar mensajes en cualquier secuencia. Esta flexibilidad es crucial para la escalabilidad y la adaptabilidad del sistema, permitiendo que los actores respondan dinámicamente a las condiciones cambiantes del sistema.

Además, los actores pueden modificar su comportamiento en respuesta a los mensajes recibidos, lo que permite una gran variedad de interacciones dinámicas y adaptativas. Por ejemplo, un actor puede cambiar de un comportamiento de 'espera' a 'procesamiento activo' una vez que recibe un cierto tipo de mensaje, lo que permite a los sistemas basados en actores ser extremadamente versátiles y reactivos a su entorno.

Estas semánticas operacionales subrayan la capacidad del modelo de actores para construir sistemas distribuidos complejos y robustos. Al adherirse a estos principios, los desarrolladores pueden diseñar sistemas que son tanto eficientes en su ejecución como resilientes a fallos y cambios en el entorno operativo."

### **Diapositiva 11: Configuraciones de Actores (Juan)**

llegamos al concepto de configuraciones de actores, que describe el estado global de un sistema de actores en un momento dado. Una configuración incluye no solo los actores presentes y sus estados internos, sino también los mensajes que están en tránsito en ese momento.

Las configuraciones de actores nos permiten modelar formalmente la evolución de un sistema a lo largo del tiempo. A medida que los actores envían y procesan mensajes, la configuración del sistema cambia, reflejando la naturaleza dinámica de estos sistemas.

### **Diapositiva 12: Modelo Conceptual (Fredy)**

"Avanzando en nuestra exploración del modelo de actores, llegamos al núcleo de su estructura teórica: el modelo conceptual. Este modelo no solo proporciona una abstracción para representar los actores y sus interacciones, sino que también establece el marco dentro del cual se definen las propiedades de concurrencia, asincronía y distribución. En esencia, el modelo conceptual actúa como el lienzo sobre el cual se pintan los sistemas distribuidos, permitiendo a los diseñadores y desarrolladores conceptualizar y construir soluciones complejas de manera intuitiva y eficaz.

En este contexto, un 'actor' se define no solo por su capacidad para procesar mensajes, crear nuevos actores y cambiar su estado interno, sino también por su identidad única dentro del sistema. Esta identidad permite que los actores sean referenciados y comunicados a través de la red, independientemente de su ubicación física, lo que es fundamental para la construcción de sistemas distribuidos.

El modelo conceptual subraya la importancia de las interacciones entre actores como el mecanismo principal para la ejecución de tareas y la coordinación dentro del sistema. Por ejemplo, en un sistema de comercio electrónico, actores individuales podrían representar usuarios, carritos de compras, productos y sistemas de pago, cada uno interactuando con los demás de manera asincrónica para completar transacciones.

Este enfoque basado en actores y sus interacciones ofrece varias ventajas, incluida la capacidad de descomponer sistemas complejos en componentes manejables, la facilidad de escalamiento y la robustez frente a fallos. Al centrarse en las interacciones en lugar de los detalles de implementación, el modelo conceptual fomenta el diseño de sistemas que son inherentemente flexibles y adaptativos, capaces de evolucionar y escalar en respuesta a las demandas cambiantes."

### **Diapositiva 13: Propiedades del Modelo (Juan)**

Una de las propiedades más significativas es la concurrencia, que permite a los actores operar  sin interferencia directa y es lo que les manejar tareas complejas y cargas de trabajo voluminosas de manera eficiente.

Otra propiedad fundamental es la transparencia de ubicación. Los actores pueden comunicarse entre sí sin conocer su ubicación física, lo que permite una flexibilidad y escalabilidad enormes en el despliegue de aplicaciones. Esta transparencia es crucial cuando los actores están ubicados en diferentes servidores o incluso en diferentes centros de datos.

Además, el modelo de actores promueve la tolerancia a fallos mediante el aislamiento. Los sistemas pueden diseñarse para detectar fallos y reaccionar adecuadamente, ya sea reiniciando actores fallidos o redistribuyendo tareas, lo que asegura una alta disponibilidad y fiabilidad.

Estas propiedades—concurrencia, transparencia de ubicación y tolerancia a fallos—son pilares que sostienen el modelo de actores

**Diapositiva 14: Concurrencia (Fredy)**

"Una de las ventajas más notables del modelo de actores es su enfoque hacia la concurrencia. A diferencia de los modelos de programación tradicionales que se basan en hilos y bloqueos para gestionar el acceso concurrente a recursos compartidos, el modelo de actores ofrece una solución elegante y eficaz a través de la encapsulación y el aislamiento. Cada actor maneja sus mensajes de entrada de manera secuencial, lo que elimina la necesidad de bloqueos y reduce significativamente la complejidad asociada con la programación concurrente.

La concurrencia en el modelo de actores no solo simplifica el desarrollo de software, sino que también mejora el rendimiento y la escalabilidad de las aplicaciones. Al permitir que múltiples actores operen en paralelo, los sistemas pueden aprovechar al máximo los recursos de hardware disponibles, distribuyendo la carga de trabajo de manera eficiente a través de múltiples núcleos o máquinas.

Además, la concurrencia facilitada por el modelo de actores es intrínsecamente segura. Dado que los actores no comparten estado y se comunican exclusivamente a través del intercambio de mensajes, se eliminan las condiciones de carrera, lo que hace que los programas sean más fiables y fáciles de razonar. Este enfoque hacia la concurrencia segura es particularmente valioso en entornos de producción, donde la confiabilidad y la estabilidad son críticas.

### **Diapositiva 15: Comunicación entre Actores (Juan)**

el modelo de actores adopta un enfoque basado en mensajes. Esto significa que los actores se comunican exclusivamente enviando y recibiendo mensajes de manera asincrónica

Los actores pueden enviar mensajes sin esperar una respuesta inmediata, lo que les permite continuar su procesamiento y responder a otros eventos entrantes.

Para ilustrar, consideremos un sistema de gestión de pedidos en línea. Un actor podría ser responsable de recibir pedidos, mientras que otros actores podrían gestionar el inventario, el procesamiento de pagos y la logística de envío. Estos actores se comunican entre sí a través de mensajes, como 'pedido recibido', 'verificar stock' o 'confirmar pago', coordinando el proceso completo de manera asincrónica y eficiente.

### **Diapositiva 16: Identificación y Direcciones de Actores (Fredy)**

"Un aspecto fundamental en la comunicación entre actores es el concepto de identificación y direccionamiento. Para que un actor envíe un mensaje a otro, debe saber cómo 'encontrarlo' dentro del sistema. Esto se logra a través de identificadores únicos o direcciones, que funcionan similar a las direcciones de correo electrónico, permitiendo que los mensajes sean enviados a actores específicos, independientemente de su ubicación física en el sistema distribuido.

La identificación de actores no solo facilita la entrega de mensajes, sino que también contribuye a la escalabilidad y flexibilidad del sistema. Los actores pueden ser movidos, replicados o reemplazados, y mientras mantengan su identificador, la comunicación puede continuar sin interrupción. Esto es crucial para sistemas que requieren alta disponibilidad y para estrategias de escalado y balanceo de carga.

Además, el sistema de identificación permite la creación dinámica de actores. Los actores pueden generar nuevos actores como respuesta a cambios en la carga de trabajo o a requisitos funcionales, asignándoles identificadores únicos que permiten su integración inmediata en el sistema.

Este mecanismo de identificación y direccionamiento subraya la flexibilidad inherente al modelo de actores, permitiendo la construcción de sistemas distribuidos que son verdaderamente dinámicos y capaces de adaptarse a condiciones cambiantes con mínima interrupción."

### **Diapositiva 17: Supervisión y Tolerancia a Fallos (Juan)**

En este modelo, los actores pueden actuar como supervisores de otros actores, monitoreando su ejecución y respondiendo a fallos. Este mecanismo de supervisión se basa en la filosofía de 'dejar fallar', donde se permite que los actores fallen sin afectar al sistema en su conjunto, mientras que los supervisores deciden la mejor manera de recuperarse de estos fallos.

Cuando un actor supervisado falla, su supervisor es notificado y puede tomar acciones como reiniciar el actor fallido, reemplazarlo por otro, o escalar el fallo según sea necesario. Esta estrategia de manejo de fallos asegura que los problemas sean localizados y gestionados

En lugar de intentar evitar fallos a toda costa, el modelo asume que los fallos son inevitables y se enfoca en la recuperación rápida y eficiente. Esto resulta en sistemas que pueden mantener un alto nivel de servicio incluso en presencia de problemas

### **Diapositiva 18: Ciclo de Vida de los Actores (Fredy)**

"Finalmente, es crucial entender el ciclo de vida de los actores dentro del modelo de actores, ya que proporciona una visión completa de cómo se crean, operan y terminan los actores. El ciclo de vida comienza con la creación del actor, generalmente instanciado por otro actor que actúa como su supervisor. Una vez creado, el actor está listo para recibir y procesar mensajes, ejecutando acciones específicas basadas en su comportamiento definido.

Durante su vida, un actor puede crear otros actores, enviar y recibir mensajes, y modificar su propio estado. También puede ser suspendido o reanudado, lo que permite optimizar el uso de recursos en el sistema. Eventualmente, un actor puede terminar su ejecución, ya sea completando su tarea, por una decisión explícita para detenerlo, o como resultado de un fallo.

El ciclo de vida de los actores es gestionado meticulosamente dentro del modelo para asegurar una ejecución eficiente y una gestión de recursos optimizada. Los supervisores juegan un rol crucial aquí, no solo en la detección y recuperación de fallos, sino también en la gestión del ciclo de vida de los actores supervisados, lo que subraya la naturaleza autónoma y autoorganizada de los sistemas basados en actores.

Este entendimiento del ciclo de vida es fundamental para diseñar sistemas que sean tanto eficientes como resilientes, aprovechando la naturaleza dinámica y adaptable del modelo de actores para construir aplicaciones robustas y escalables."

### **Diapositiva 19: Implementación (Fredy)**

"Al pasar de la teoría a la práctica, la implementación del modelo de actores en sistemas reales requiere una comprensión profunda tanto de sus principios fundamentales como de las herramientas y lenguajes disponibles. La implementación efectiva del modelo de actores se centra en cómo los actores se crean, se comunican y se gestionan dentro de un entorno de ejecución, asegurando que el sistema sea escalable, resiliente y fácil de mantener.

Herramientas y frameworks como Akka para Java y Scala, Orleans para .NET y Erlang/OTP son ejemplos prominentes que facilitan la implementación del modelo de actores, proporcionando abstracciones de alto nivel y manejo eficiente de los actores y sus interacciones. Estas plataformas ofrecen características avanzadas como supervisión, tolerancia a fallos, y distribución transparente, permitiendo a los desarrolladores concentrarse en la lógica de negocio en lugar de en la infraestructura subyacente.

Además, la implementación efectiva requiere consideraciones sobre el diseño del sistema, incluyendo la modelización de actores, la definición de mensajes y la estructuración de las interacciones entre actores. Es crucial diseñar actores que sean cohesivos, con responsabilidades claras y bien definidas, y que interactúen de manera clara y eficiente para realizar las tareas del sistema.

En resumen, la implementación del modelo de actores en aplicaciones prácticas es un proceso que combina principios teóricos sólidos con herramientas y técnicas de software modernas. Esta combinación permite construir sistemas distribuidos que no solo son poderosos y eficientes sino también robustos y fáciles de operar y mantener."

### **Diapositiva 20: Implementación con Golang (Juan)**

"Golang, o Go, se ha destacado como un lenguaje de programación eficaz para la implementación de sistemas concurrentes y distribuidos.. Aunque Go no proporciona un marco de actores de forma nativa, su enfoque en la concurrencia con goroutines y canales se alinea bien con el modelo de actores

En Go, las goroutines funcionan como actores ligeros que pueden ejecutarse en paralelo, mientras que los canales permiten la comunicación segura y sincronizada (o no sincronizada) entre ellas.

Para implementar un actor en Go, se podría definir una goroutine que encapsule el estado y el comportamiento del actor, y utilice canales para recibir mensajes y comunicarse con otros actores.

En este ejemplo implementamos un sistema de actores simple en Go, En el que actores locales y remotos envian mensajes. Inicialmente, se define un actor básico que puede recibir y enviar mensajes a través de un canal. Luego, se expande este concepto con un "ActorManager" que gestiona múltiples actores, facilitando el registro y la comunicación entre ellos.

Para soportar actores remotos, se utiliza RPC, permitiendo que los actores envíen mensajes a través de la red, esto mantiene el código desacoplado y fácil de manejar.

### **Diapositiva 21: Ejemplo de un Actor Simple en Golang (Fredy)**

Creamos un actor y llamamos al método Receive, luego el método Send, permite a este actor recibir mensajes enviados por otros actores
```go
type Actor struct {

inbox chan string

}

func NewActor() *Actor {

return &Actor{

inbox: make(chan string)

}

}

func (a *Actor) Receive() {

for msg := range a.inbox {

fmt.Println(msg)

}

]

func (a *Actor) Send(msg string) {

a.inbox <- msg

}

func main() {

actor := NewActor()

go actor. Receive()

actor. Send("Hello world!")

actor. Send("This is a message.")

}
```

Este código en Go define un sistema básico de actores. Primero, define una estructura `Actor` con un canal `inbox` para recibir mensajes tipo `string`. La función `NewActor` inicializa un actor, creando el canal `inbox`. La función `Receive` del actor escucha continuamente el canal `inbox` para nuevos mensajes, imprimiéndolos cuando llegan. La función `Send` permite enviar un mensaje al canal `inbox` del actor. En `main`, se crea un actor, se inicia su método `Receive` en una goroutine para que escuche mensajes de forma concurrente, y se envían dos mensajes al actor usando `Send`.

### **Diapositiva 22: Ejemplo de un Actor Simple en Golang parte 2 (Juan)**

Para conseguir la comunicación necesitamos soporte para enrutamiento local y remoto

En este caso el type **ActorManager** es una colección de actores y proporciona métodos para registrar actores y enviar mensajes entre ellos

```go
package main
import (
"fmt"
"net/rpc"
}
```
Importa los paquetes necesarios para el programa, incluyendo "fmt" para la entrada/salida y "net/rpc" para la comunicación entre procesos remotos.
```go
type Message struct {
To string
From string
Body string
}
```
Define una estructura Message que representa un mensaje con campos To (destinatario), From (remisor) y Body (cuerpo del mensaje).
```go
type Actor struct {
Name string
Messages []Message
}
```
Define una estructura Actor que representa un actor con un nombre y una lista de mensajes.
```go
func (a "Actor) SendMessage(m Message) {
a.Messages = append(a.Messages, m)
}
```
Define un método SendMessage asociado a la estructura Actor que agrega un mensaje a la lista de mensajes del actor.
```go
func (a "Actor) ProcessMessages() {
    for _, m := range a.Messages {
    fmt.Printf("Actor %s received message: %s\\n" a.Name m.Body)
    }
    a.Messages = nil
}
```	
Define un método ProcessMessages asociado a la estructura Actor que imprime todos los mensajes recibidos por el actor y luego limpia la lista de mensajes.
```go
type ActorManager struct {
    Actors map[string]"Actor
}
```
Define una estructura ActorManager que contiene un mapa de actores indexado por sus nombres.
```go
func NewActorManager() *ActorManager {
    return &ActorManager(Actors: make(map[string]"Actor)}
}
```
define una función NewActorManager que contiene un mapa vacío de actores y devuelve un puntero inicializado.
```go
func (s "ActorManager) RegisterActor(name string) {
    s.Actors[name] = &Actor{Name: name}
}
```
Define un método RegisterActor asociado a la estructura ActorManager que registra un nuevo actor en el gestor de actores. Este método crea un nuevo actor con el nombre especificado y lo agrega al mapa de actores del gestor
```go
func (s *ActorManager) SendMessage(m Message) {
    if actor ok := s.Actors[m. To]; ok {
    actor. SendMessage(m)
    } else {
        // send message to remote actor
        client err := rpc.Dial("tcp" m.To)
        if err != nil {
        fmt.Printf ("Error connecting to remote actor %s: %s\\n" m.To err)
        return
        }
        defer client.Close()
        var reply string
        err = client.Call("RemoteActor. ReceiveMessage" m &reply)
        if err != nil {
            fmt.Printf("Error sending message to remote actor %s: %s\\n" m. To err)
            return
        }
    }
}
```

Define un método SendMessage asociado a la estructura ActorManager que envía un mensaje a un actor específico. Si el actor está presente en el gestor de actores, el mensaje se envía al actor local utilizando el método SendMessage del actor. Si el actor no está presente localmente, se asume que es remoto y se intenta enviar el mensaje utilizando RPC. Si ocurre algún error durante la conexión o el envío del mensaje remoto, se imprime un mensaje de error.

### **Diapositiva 23: Ejemplo de un Actor Simple en Golang (Fredy)**

En este caso el type **RemoteActor** representa un actor que puede recibir mensajes a través de una red

**RemoteActor** implementa el método **ReceiveMessage** para imprimir el mensaje recibido a consola y retornar un mensaje de respuesta

La función **main** ejemplo registra dos actores locales y envía mensajes a estos y a un actor remoto en localhost:1234

```go
type RemoteActor struct{}

func (a *RemoteActor) ReceiveMessage(m Message reply string) error {
    fmt. Printf ("Remote actor %s received message: %s\\n" m. To m. Body)
    *reply = "Message received"
    return nil
}

func main() {
    // create local actor system
    actorManager := NewActorManager()
    // register local actors
    actorManager. RegisterActor("actor1")
    actorManager. RegisterActor ("actor2")
    // send message to local actor
    actorManager . SendMessage (Message{
        To: "actor1"
        From: "actor2"
        Body: "Hello from actor2 to actor1"
        })

    // send message to remote actor
    actorManager. SendMessage (Message{
        To: "localhost: 1234"
        From: "actor1"
    Body: "Hello from actor1 to remote actor on localhost: 1234"
    })

    // process messages in all actors
    for _ actor := range actorManager. Actors {
        actor. ProcessMessages ()
    }
}
```

Este código implementa un sistema básico para la gestión de actores en Go, donde `ActorManager` administra actores y facilita el envío de mensajes tanto local como remotamente. `Actor` representa una entidad que puede recibir y procesar mensajes. `ActorManager` puede registrar nuevos actores y enviar mensajes. Si el destinatario está registrado localmente, el mensaje se maneja internamente; si no, intenta enviar el mensaje a un actor remoto usando RPC, gestionando conexiones y posibles errores en la comunicación.

### **Diapositiva 24: Ejemplo de un Actor Simple en Golang (Juan)**

Este snippet de código inicia un actor remoto en localhost:1234
```go
import (
"fmt"
"net"
"net/rpc"
)

type Message struct {
    To string
    From string
    Body string
}

type RemoteActor struct{}

func (a *RemoteActor) ReceiveMessage(m Message reply string) error {
    fmt.Printf("Remote actor %s received message: %s\\n" m. To m.Body)
    *reply = "Message received"
    return nil
}

func main() {
    actor := new(RemoteActor)
    rpc. Register(actor)
    1 e := net. Listen("tcp" "localhost :1234")
    if e != nil {
        fmt.Printf("Error listening: %s\\n" e)
        return
    }
    defer 1.Close()
    fmt.Println("Remote actor listening on localhost: 1234")
    rpc.Accept (1)
}
```

Una vez este actor este activo podemos correr la funcion **main** anterior y monitorear los actores locales

Actor actor1 received message: Hello from actor2 to actor1

Y para el actor remoto

Remote actor listening on localhost:1234

Remote actor localhost:1234 received message: Hello from actor1 to remote actor on localhost:1234

Este fragmento de código inicia un servidor RPC en Go que escucha en el puerto 1234 para un actor remoto. Define una estructura `Message` para los mensajes y un `RemoteActor` que implementa un método `ReceiveMessage` para procesar mensajes recibidos. El servidor se inicia, registrando el actor remoto y esperando conexiones entrantes. Cuando un mensaje es recibido, se imprime y se responde. Este ejemplo ilustra cómo implementar un actor remoto básico utilizando el paquete `net/rpc` de Go.

### **Diapositiva 25: Casos de Uso del Modelo de Actores (Fredy)**

"El modelo de actores no es solo una construcción teórica; su aplicación práctica se extiende a una variedad de dominios y casos de uso, demostrando su versatilidad y eficacia. Desde sistemas de procesamiento de transacciones hasta aplicaciones de Internet en tiempo real y sistemas de simulación, el modelo de actores ofrece un marco robusto para la construcción de sistemas concurrentes y distribuidos.

Uno de los casos de uso más prominentes es en el desarrollo de sistemas de telecomunicaciones, donde la necesidad de manejar miles de conexiones simultáneas de manera eficiente es crítica. El modelo de actores permite gestionar cada conexión como un actor independiente, facilitando un manejo de estado y una concurrencia eficiente sin bloqueos, lo que es esencial para mantener altos niveles de rendimiento y disponibilidad.

En el ámbito de las aplicaciones web y móviles, el modelo de actores se utiliza para construir back-ends escalables que pueden manejar una gran cantidad de usuarios y datos en tiempo real. Frameworks como Akka en Scala y Orleans en .NET han popularizado el uso del modelo de actores para desarrollar aplicaciones que requieren un alto grado de interactividad y una respuesta rápida a eventos en tiempo real.

Además, el modelo de actores se ha aplicado con éxito en el campo de la inteligencia artificial y el procesamiento de datos a gran escala. Sistemas que requieren la coordinación de múltiples tareas de procesamiento y análisis de datos pueden beneficiarse de la capacidad del modelo de actores para descomponer el problema en actores que pueden procesar datos y aprender de manera independiente, optimizando el uso de recursos y acelerando el tiempo de procesamiento.

### **Diapositiva 26: Ejemplo de un Posible Uso del Modelo (Juan)**

Video **[A brief introduction to the actor model & distributed actors](notion://www.notion.so/fredyrosero/[aqu%C3%AD](https://www.youtube.com/watch?v=YTQeJegJnbo).)

El video introduce el modelo de actores, destacando su idoneidad para construir sistemas masivamente concurrentes, como los necesarios para dispositivos inteligentes en hogares. Contrasta los desafíos de la programación tradicional con la eficiencia del modelo de actores en manejar la concurrencia a través de procesos ligeros e aislados. Estos procesos se comunican mediante el paso de mensajes, mejorando la tolerancia a fallos y la capacidad de respuesta del sistema. Las ventajas del modelo de actores, incluido su soporte inherente para sistemas distribuidos y tolerancia a fallos a través de la supervisión de procesos, se destacan como soluciones para el desarrollo de aplicaciones escalables y fiables para aplicaciones modernas e interconectadas.

### **Diapositiva 27: Conclusiones (Fredy)**

"En conclusión, el modelo de actores representa una abstracción poderosa y flexible para el desarrollo de sistemas concurrentes y distribuidos. A lo largo de esta presentación, hemos visto cómo facilita la comunicación asincrónica, gestiona la concurrencia de manera segura y mejora la tolerancia a fallos a través de la supervisión y recuperación.

Una de las mayores fortalezas del modelo es su capacidad para modelar el mundo real de una manera intuitiva, permitiendo a los desarrolladores conceptualizar problemas complejos en términos de actores y mensajes. Esto no solo simplifica el diseño de sistemas distribuidos sino que también abre la puerta a la innovación y la eficiencia en la implementación.

Adoptar el modelo de actores puede transformar radicalmente cómo se abordan los desafíos de la computación distribuida, ofreciendo una ruta hacia sistemas más robustos, escalables y fáciles de mantener. Como hemos visto a través de varios ejemplos y aplicaciones, su versatilidad lo hace adecuado para una amplia gama de dominios y problemas."

### **Diapositiva 28: Pros y Contras del Modelo de Actores (Juan)**

“Ya vimos que el modelo de actores se destaca por su **escalabilidad**, que facilita el crecimiento del sistema sin comprometer su rendimiento.

Por su **tolerancia a fallos** porque al aislar los errores en un actor no afectan directamente a los demás.

La **transparencia de ubicación** facilita la distribución de carga y la comunicación en sistemas distribuidos.

mantener **estados internos privados** asegura la seguridad de los datos y la integridad del sistema porque limita el acceso al estado interno de los actores por mensajes definidos.

Sin embargo, el modelo de actores puede ser **susceptible a deadlocks**, especialmente en sistemas con complejas dependencias de comunicación, donde múltiples actores esperan respuestas el uno del otro sin avanzar. Además, existe el riesgo de **overflow en los buzones** de mensajes de los actores cuando la producción de mensajes supera la capacidad de procesamiento, lo que puede llevar a la pérdida de mensajes o a la degradación del rendimiento del sistema. Estos contras pueden ser solucionados con un diseño cuidadoso y estrategias de manejo de errores para mitigar los impactos negativos en la robustez y la fiabilidad del sistema.

Pese a estos desafíos, el modelo de actores sigue siendo una herramienta valiosa para el diseño de sistemas distribuidos, proporcionando un conjunto de principios y mecanismos que, cuando se aplican correctamente, pueden ofrecer soluciones eficientes a problemas complejos de concurrencia y distribución."