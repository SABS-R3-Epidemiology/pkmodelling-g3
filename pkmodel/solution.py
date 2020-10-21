#
# Solution class
#

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------
    
    model: an object in the Model Class
    protocol: an object in the Protocol Class
    T: The system is solved for the time interval [0, T]

    """
    def __init__(self, model, protocol, T):
        self.model, self.protocol, self.T = model, protocol, T

    # Solve the system of ODEs
    def solve(self):
    
        # Build up the system of ODEs
        if self.model.dosing_type == "intravenous":
        
            # Assuming q = [q1, ..., qn, qc], Q = [Q1, ..., Qn], V = [V1, ..., Vn, Vc]
            def f(t, q, Q, V):
                dydt = []
                
                # Differential equations for the peripheral compartments q1, ..., qn
                for i in [0:self.model.number_of_compartments]:
                    dydt.append(Q[i]*(q[-1]/V[-1] - q[i]/V[i])
                
                # Differential equation for the central compartment qc
                # Assuming protocol is the Dose(t) function
                # ??? Sum can be used as below?
                dydt.append(self.protocol - (q[-1]/V[-1]) * self.model.CL - sum(dydt))
                return dydt
        
            t_span = (0, T)
        
            # ? Initial conditions
            q_init = [0] * (model.number_of_compartments + 1)
        
            Q, V = sel.model.Q, self.model.V
        
            sol = solve_ivp(lambda t, q: f(t, q, Q, V), t_span, q_init)
        
            return sol
        
        elif self.model.dosing_type == "subcutanous":
        
            # Assuming q = [q1, ..., qn, qc, q0], Q = [Q1, ..., Qn], V = [V1, ..., Vn, Vc]
            def f(t, q, Q, V):
                dydt = []
                
                # Differential equations for the peripheral compartments q1, ..., qn
                # Note that the position of qc becomes -2
                for i in [0:self.model.number_of_compartments]:
                    dydt.append(Q[i]*(q[-2]/V[-1] - q[i]/V[i])
                
                # Differential equation for the central compartment qc
                # Assuming protocol is the Dose(t) function
                # ??? Sum can be used as below?
                dydt.append(self.model.k_a * q[-1] - (q[-2]/V[-1]) * self.model.CL - sum(dydt))
                # Differential equation for q0
                dydt.append(self.protocol - self.model.k_a * q[-1])
                
                return dydt
        
            t_span = (0, T)
        
            # ? Initial conditions
            q_init = [0] * (model.number_of_compartments + 2)
        
            Q, V = sel.model.Q, self.model.V
        
            sol = solve_ivp(lambda t, q: f(t, q, Q, V), t_span, q_init)
        
            return sol
                
    
    
