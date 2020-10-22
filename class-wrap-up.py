"""CLASS-WRAP-UP

Construct behaviour of a system given inputs for model and protocol by the user.
Makes use of Protocol, Model and Solution classes in the pkmodel module.

Behaviours represented for one or more dosing protocols are to be plotted
individually and in comparision.

"""
from pkmodel import Protocol, Model, Solution
import matplotlib.pylab as plt
import numpy as np

def plot_behaviour_model_with_protocol( model, protocol, t_time = 1000):
    """Plots behaviour over time of one treatment, given the model and the dosing protocol.

    Parameters
    ----------
    model: Model class object; the compartment-based model of the system on which
    the drug is administered.
        an example: Model()

    protocol: Protocol class object; the dosing protocol under which the drug 
    is administered to the patient. 
        an example: Protocol()
    
    t_time: integer, optional; total time on which we evaluate behaviour of drug
        an example: Model()
    """
    # Time scale on which to plot the behaviour
    t_eval = np.linspace(0, 1, t_time) 

    # Create solution of model and protocol
    solution = Solution(model, protocol, t_time)

    fig = plt.figure(figsize=())
    plt.plot(solution.t, solution.y[0, :], label = model + '- q_c')
    for i in range(model.num_periph):
        plt.plot(solution.t, solution.y[i+1, :], label = model + '- q_p'+str(i+1))
    
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()
        

    
    
