# Parcial_2SD
Desarrollo del parcial

## Parte Conceptual 
1. ¿Cuál es la diferencia entre un latch y un flip flop?, además ¿cuáles son los
diferentes tipos de latch y flip flops?, explique por favor las
características

R// Flip-Flop: Son los bloques fundamentales de construccion de los circuitos digitales secuenciales, tienen la capacidad de almacenar un bit de informacion ademas de que es un dispositivo con dos estados estables que se utilizan para representar 0 y el 1 binario 

Latch: Es un dispositivo de almacenamiento biestable que es sensible al nivel (activo mientras la señal de control esté en un estado alto o bajo), cambia su estado cuando cambian las entradas es más simple pero menos controlado 

<img width="796" height="274" alt="image" src="https://github.com/user-attachments/assets/76768306-c38b-4a7c-83d8-d35a47a26eb0" />


### Tipos y caracteristicas: 

FLIP FLOP SR (Ser-Reset): Es el tipo mas basico de celda de memoria, su funcionamiento se basa en dos entradas principales 

Set(S): Establece la salida en alto(1)

Reset(R): La establece en bajo(0)


FLIP-FLOP JK(Universal): Es una version mejorada del SR que elimina el estado invalido mediante una retroalimentacion interna es considerado versatil

Su caracterisitca distintiva es el estado de Basculacion cuando ambas entradas J y K estan en alto(1) y la salida cambia al estado opuesto en cada pulso de relok

FLIP- FLOP D: captura el valor de la entrada D en el flanco del reloj y lo mantiene en la salida Q

<img width="694" height="227" alt="image" src="https://github.com/user-attachments/assets/a0ff9a29-27cb-4295-bf12-c7f8e792dcfb" />

FLIP-FLOP T: Cambia o bascula el estado de la salida si la entrada T es 1, si T es 0 mantiene el estado anterior 
<img width="694" height="207" alt="image" src="https://github.com/user-attachments/assets/324528d9-ec79-46ca-ad71-9d433ef85758" />


2. ¿Cuál es la diferencia entre un multiplexor y un demultiplexor?. Desarrollar
la explicación de un multiplexor 8 entradas y un demultiplexor de 8 salidas.

Un multiplexor (MUX) y un demultiplexor (DEMUX) son circuitos digitales que hacen operaciones opuestas. El multiplexor actúa como un selector: recibe varias entradas de datos y, dependiendo de las líneas de selección, elige una sola y la envía a la salida. El demultiplexor hace exactamente lo contrario: recibe una sola entrada y, según las líneas de selección, la dirige hacia una de sus múltiples salidas.

Un multiplexor de 8 entradas (8:1) recibe 8 señales de datos (I₀ a I₇) y necesita 3 líneas de selección (S₀, S₁, S₂), ya que con 3 bits se pueden representar 2³ = 8 combinaciones posibles. Dependiendo del valor binario que tengan las líneas de selección, la salida Y tomará el valor exacto de la entrada apuntada

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/dc5783f8-11a8-41d3-9159-cd40f3bc7618" />


Un demultiplexor de 8 salidas (1:8) recibe una sola señal de entrada y también usa 3 líneas de selección para decidir a cuál de sus 8 salidas (Y₀ a Y₇) enviarla. Las demás salidas permanecen en 0. Si S₂S₁S₀ = 011, la señal de entrada aparece únicamente en Y₃, y el resto quedan apagadas. Es la operación inversa al MUX: en lugar de concentrar muchas señales en una, distribuye una señal hacia muchos destinos posibles

<img width="420" height="359" alt="image" src="https://github.com/user-attachments/assets/e5ee0719-b7e7-4780-a15c-37ce25cb4fc8" />


4. Explicar de forma sencilla qué es un sumador completo, un sumador medio y
circuitos secuenciales.

Un sumador medio es el circuito digital más básico para sumar. Toma dos bits (A y B) y produce dos resultados: la suma (S), que se obtiene con una compuerta XOR, y el acarreo de salida (C), que se obtiene con una compuerta AND. Su limitación es que no puede recibir un acarreo proveniente de una etapa anterior, por lo que solo sirve para sumar los bits menos significativos de un número.

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/407f20eb-0606-4923-ae84-77e85f30a114" />


sumador completo (Full Adder), que suma tres bits: A, B y un acarreo de entrada (Cin) que viene de una etapa previa. Produce igualmente una suma S y un acarreo de salida Cout. Su gran ventaja es que varios sumadores completos se pueden encadenar en serie, donde el Cout de uno se convierte en el Cin del siguiente, permitiendo sumar números de cualquier cantidad de bits


<img width="551" height="542" alt="image" src="https://github.com/user-attachments/assets/5e785e88-8535-4ebe-8ed5-93847ce4eb2c" />


Los circuitos secuenciales representan un concepto más amplio y más poderoso. A diferencia de los circuitos combinacionales, donde la salida depende únicamente de las entradas en ese instante, en los circuitos secuenciales la salida depende de las entradas actuales y también del estado anterior del circuito, es decir, tienen memoria

<img width="397" height="249" alt="image" src="https://github.com/user-attachments/assets/bf70abe6-6d93-4f64-9781-8e7ad5fd6064" />


6. ¿Qué es un mapa de karnaugh? Y ¿para qué sirve?

Es una herramienta gráfica para simplificar expresiones booleanas sin usar álgebra. Organiza todas las combinaciones posibles de variables en una cuadrícula donde las celdas adyacentes difieren en solo 1 bit (código Gray), sirve para minimizar funciones lógicas, es decir, obtener el circuito digital más simple posible con el menor número de compuertas, lo que reduce costo, tamaño y consumo.


## Parte de diseño 

2A

𝑋 = 𝐴𝐵ത (𝐶 + 𝐵𝐷 + 𝐴ҧ𝐵ത) c

CIRCUITO:


<img width="1310" height="734" alt="image" src="https://github.com/user-attachments/assets/31686dd1-a952-417f-a1cb-55248a44c1de" />


Desarrollar tabla de verdad a partir de la ecuación
<img width="1243" height="408" alt="image" src="https://github.com/user-attachments/assets/930ed96a-1a38-4244-8e7b-158f9d31e9f8" />




2B

𝑋 = 𝐴𝐵ത𝐶 𝐵𝐷 + 𝐶𝐷𝐸 + 𝐴C

CIRCUITO:
<img width="1660" height="960" alt="image" src="https://github.com/user-attachments/assets/bad70eba-8b39-44cc-8253-a10abcd0932b" />


Desarrollar tabla de verdad a partir de la ecuación

<img width="1188" height="668" alt="image" src="https://github.com/user-attachments/assets/42c59df5-a425-469f-ba19-9369f1c94b8e" />





