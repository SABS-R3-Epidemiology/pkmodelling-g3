#
# Solution class
#

import numpy as np
from pkmodel import Model, Protocol

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------
    
    model: an object in the Model Class
    protocol: an object in the Protocol Class
    T: The system is solved for the time interval [0, T]
    num_t: The computed solution is stored at num_t evenly spaced times in the interval [0, T]

    """
    def __init__(self, model, protocol, T, num_T):
        self.model, self.protocol, self.T, self.num_T = model, protocol, T, num_T
        if not isinstance(model, Model):
            raise TypeError('Not correct type for model, please use Model class')
        if  not isinstance(protocol, Protocol):
            raise TypeError('Not correct type for protocol, please use Protocol class')

    # Solve the system of ODEs
    @property
    def solve(self):
        """Solves the system of ODEs created by the protocol and model.
        """
        # Build up the system of ODEs
        if self.model.dosing_type == "intravenous":
        
            # Assuming q = [q1, ..., qn, qc], Q = [Q1, ..., Qn], V = [V1, ..., Vn, Vc]
            def f(t, q, Q, V):
                dydt = []
                
                # Differential equations for the peripheral compartments q1, ..., qn
                for i in range(self.model.num_perph):
                    dydt.append(Q[i]*(q[-1]/V[-1] - q[i]/V[i]))
                
                # Differential equation for the central compartment qc
                # Assuming protocol is the Dose(t) function
                # ??? Sum can be used as below?
                dydt.append(self.protocol - (q[-1]/V[-1]) * self.model.CL - sum(dydt))
                return dydt
            
            # Solve the system of ODEs for the time span [0, T]
            t_span = (0, T)
        
            # ? Initial conditions
            q_init = [0] * (model.number_of_compartments + 1)
        
            Q = self.model.Q_P
            V = self.model.V_P.append(V_C)
        
            sol = solve_ivp(lambda t, q: f(t, q, Q, V), t_span, q_init, t_eval = np.linspace(0, self.T, num = self.num_t))
        
            return sol
        
        elif self.model.dosing_type == "subcutanous":
        
            # Assuming q = [q1, ..., qn, qc, q0], Q = [Q1, ..., Qn], V = [V1, ..., Vn, Vc]
            def f(t, q, Q, V):
                dydt = []
                
                # Differential equations for the peripheral compartments q1, ..., qn
                # Note that the position of qc becomes -2
                for i in range(self.model.num_perph):
                    dydt.append(Q[i]*(q[-2]/V[-1] - q[i]/V[i]))
                
                # Differential equation for the central compartment qc
                # Assuming protocol is the Dose(t) function
                # ??? Sum can be used as below?
                dydt.append(self.model.k_a * q[-1] - (q[-2]/V[-1]) * self.model.CL - sum(dydt))
                # Differential equation for q0
                dydt.append(self.protocol - self.model.k_a * q[-1])
                
                return dydt
            
            # Solve the system of ODEs for the time span [0, T]
            t_span = (0, T)
        
            # ? Initial conditions
            q_init = [0] * (model.number_of_compartments + 2)
        
            Q = self.model.Q_P
            V = self.model.V_P.append(V_C)
        
            sol = solve_ivp(lambda t, q: f(t, q, Q, V), t_span, q_init, t_eval = np.linspace(0, self.T, num = self.num_t))
        
            return sol
                
    
    
