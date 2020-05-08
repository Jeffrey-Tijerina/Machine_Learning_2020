# History of the Perceptron

The Perceptron model was based off of work done primarily by Santiago Ramon y Cajal and Sir Charles Scott Sherrington. Santiago Ramon y Cajal was primarily known for his work on the structure of nervous tissue and showed that neurons were physically seperate from each other despite being able to communicate with one another. Understanding this was fundamental to understanding the structure of the brain and a great effort to plainly describe the behavior of neurons was done by William James.


Donald Hebb published a paper in 1949 based off of the work of McCulloch-Pitts that would help change the way artificial neurons were understood by the world. In his book, The Organization of Behavior, he states, 
>“When an axon of cell A is near enough to excite a cell B and repeatedly or persistently takes part in firing it, some growth process or metabolic change takes place in one or both cells such that A’s efficiency, as one of the cells firing B, is increased.” 

This soon came to be known as Hebb’s rule. 
Hebb's rule altered the McCulloch-Pitts neuron to weight each of the inputs. In other words, an input of 1 may be given more or less weight, relative to the total threshold sum.


Frank Rosenblatt used the McCulloch-Pitts neuron and the Hebb's work to develop the first perceptron. This perceptron, which could learn through the weighting of inputs was crucial the eventual formation of neural networks.  Rosenblatt discussed the perceptron in his 1962 book, Principles of Neurodynamics.   A basic perceptron is represented as follows:
>"This perceptron has a total of five inputs a1 through a5 with each having a weight of w1 through w5. Each of the inputs are weighted and summed at the node.  If the threshold is reached, an output results.  Of great importance is that each of the inputs may not be given equal weight. The perceptron may have “learned” to weight a1 more than a2 and so on."

The summation formula for determining whether or not the threshold (θ) is met for the artificial neuron with N inputs (a 1, a2, . . . ,  aN) and their respective weights of w 1, w2, . . . , wN  is:

![perceptron model eq](https://github.com/Jeffrey-Tijerina/Machine_Learning_2020/blob/master/Perceptron/perceptron_eq_1.jpg)

The activation function then becomes:

![perceptron model activation fn](https://github.com/Jeffrey-Tijerina/Machine_Learning_2020/blob/master/Perceptron/perceptron_eq_2.jpg)

The activation function used by McCulloch and Pitts was the threshold step function.  However, other functions that can be used are the Sigmoid, Piecewise Linear and Gaussian activation functions.
