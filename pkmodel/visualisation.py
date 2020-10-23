"""CLASS-WRAP-UP
----------------
Construct behaviour of a system given inputs for model and protocol by the user.
Makes use of Protocol, Model and Solution classes in the pkmodel module.

Behaviours represented for one or more dosing protocols are to be plotted
individually and in comparision.
----------------
"""
from pkmodel import Protocol, Model, Solution
import matplotlib.pylab as plt

def plot_behaviour_one_experiment( model, protocol, t_time = 1000):
    """Plots behaviour over time of one treatment, given the model and the dosing protocol.

    Parameters
    ----------
    model: Model class object; the compartment-based model of the system on which
    the drug is administered.
        an example: Model(0, 1,[0],[0],1, 'my_model')

    protocol: Protocol class object; the dosing protocol under which the drug 
    is administered to the patient. 
        an example: Protocol()
    
    t_time: integer, optional; total time in hours on which we evaluate behaviour of drug
        an example: 1000
    """
    # Time scale on which to plot the behaviour
    t_eval = np.linspace(0, 1, t_time) 

    # Create solution of model and protocol to be plotted
    solution = Solution(model, protocol, t_time)
    sol = solution.solve

    fig = plt.figure()
    plt.plot(solution.t, solution.y[0, :], label = model + '- q_c')
    for i in range(model.num_periph):
        plt.plot(solution.t, solution.y[i+1, :], label = model + '- q_p'+str(i+1))
    
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()
        
def plot_comparison_two_experiments(models, protocols, t_time = 1000):
    """Plots comparision graphs over time of two treatments,
    given their respective model and the dosing protocol.

    Parameters
    ----------
    models: list of Model class object; the compartment-based models of the system on which
    the drug is administered in orderof plotting
        an example: [Model(0, 1,[0],[0],1, 'my_model1'), Model()]

    protocol: Protocol class object; the dosing protocols under which the drug 
    is administered to the patient for each model chosen. 
        an example: [Protocol(), Protocol()]
    
    t_time: integer, optional; total time in hours on which we evaluate behaviour of drug
        an example: 1000
    """
    # Time scale on which to plot the behaviour
    t_eval = np.linspace(0, 1, t_time) 

    # Create solution of model and protocol to be plotted
    solution = Solution(model, protocol, t_time, t_eval)
    sol = solution.solve

    fig = plt.figure()
    plt.plot(solution.t, solution.y[0, :], label = model + '- q_c')
    for i in range(model.num_periph):
        plt.plot(solution.t, solution.y[i+1, :], label = model + '- q_p' + str(i+1))
    
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()
    
    
