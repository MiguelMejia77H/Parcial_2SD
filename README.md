# Parcial_2SD
Desarrollo del parcial

## Parte Conceptual 
1. ¿Cuál es la diferencia entre un latch y un flip flop?, además ¿cuáles son los
diferentes tipos de latch y flip flops?, explique por favor las
características

R// Flip-Flop: Son los bloques fundamentales de construccion de los circuitos digitales secuenciales, tienen la capacidad de almacenar un bit de informacion ademas de que es un dispositivo con dos estados estables que se utilizan para representar 0 y el 1 binario 

Latch: Es un dispositivo de almacenamiento biestable que es sensible al nivel (activo mientras la señal de control esté en un estado alto o bajo), cambia su estado cuando cambian las entradas es más simple pero menos controlado 


### Tipos de Flip Flops: 

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

Un demultiplexor de 8 salidas (1:8) recibe una sola señal de entrada y también usa 3 líneas de selección para decidir a cuál de sus 8 salidas (Y₀ a Y₇) enviarla. Las demás salidas permanecen en 0. Si S₂S₁S₀ = 011, la señal de entrada aparece únicamente en Y₃, y el resto quedan apagadas. Es la operación inversa al MUX: en lugar de concentrar muchas señales en una, distribuye una señal hacia muchos destinos posibles.



4. Explicar de forma sencilla qué es un sumador completo, un sumador medio y
circuitos secuenciales.


5. ¿Qué es un mapa de karnaugh? Y ¿para qué sirve?
