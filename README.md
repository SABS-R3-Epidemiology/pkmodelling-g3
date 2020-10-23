![Run on multiple OS](https://github.com/SABS-R3-Epidemiology/pkmodelling-g3/workflows/Run%20on%20multiple%20OS/badge.svg)
![Run Unit Tests](https://github.com/SABS-R3-Epidemiology/pkmodelling-g3/workflows/Run%20Unit%20Tests/badge.svg)
[![codecov](https://codecov.io/gh/SABS-R3-Epidemiology/pkmodelling-g3/branch/Package-yml/graph/badge.svg?token=AP7BXN01RK)](undefined)
[![BCH compliance](https://bettercodehub.com/edge/badge/SABS-R3-Epidemiology/pkmodelling-g3?branch=master)](https://bettercodehub.com/)
[![Documentation Status](https://readthedocs.org/projects/pkmodelling-g3/badge/?version=latest)](https://pkmodelling-g3.readthedocs.io/en/latest/?badge=latest)

# Pharmacokinetics Modelling and Drug Delivery Research

Pharmacokinetics (PK) is the branch of pharmacology responsible for the study of how different substances interact with living organisms, in particular with the way they are assimilated by said organisms. It provides a quantitative basis for the description of the delivery of a particular drug to a patient, through studying its uptake behaviour and how it diffuses in the body over time.

Any drug can have widely contrasting effects on the body depending on the quantity in which the substance is administered. Too little and the effects will not be visible due mainly to the diffusion of substances that occurs in the body, hence the concentration of the chemical will be too low in the region that it targets. At the same time, too much of the same chemical and adverse effects will be likely to appear. These mainly occur because the large quantity of the drug may not only have an effect on the particular metabolic pathway you wish to treat, but also on several others, producing too strong shifts in them that unbalance the gentle equilibrium in which they find themselves, causing large scale disruptions with observable consequences. 

There are four physiological processes that are quantified in any pharmacokinetic model of a system:
* __Adsorption__
* __Distribution__
* __Metabolism__
* __Excretion__

Such a model divides the organism into compartments, each corresponding to an organ or system of organs (e.g. blood vessels, muscle tissue) and quantifies the changes in the concentration of the drug in each compartment through a series of ordinary differential equations (ODEs). There is one central compartment through which the drug first enters the body. A number of peripheral compartments, all connected with the central one, but with no interactions present between them, may also be modelled as part of the system. This number can range from zero to many and depends on the type of treatment, i.e. which organs or system of organs it will engage until the active substance reaches its target area.

Each such model is uniquely characterised by parameters entirely dependent on the nature of the average patient and/or of the medication scheme, resulting in three factors that affect the behaviour of the drug:
* __Experiment constants:__
  * _Type of dosing_: intravenous vs subcutaneous - it affects the number of compartments we need to consider for an accurate representation of the phenomenon
  * _Dosing protocol_: rate at which the drug enters the system - the main fine tuning mechanism we would use to ensure optimum efficiency of the treatment and that no adverse effects occur due to overdosing
*  __Physiological constants:__ such as rates of diffusion within compartments, exchange rates between compartments and rate at which drug leaves the body (i.e. Clearance Rate)

Following this methodology proves to be essential in the development of new treatments, to ensure a sufficient quantity of the active substance is administered to the subject for the medicine to be effective.

# The mathematical model

The model comprises a system of ordinary differential equations (ODEs) that codify the flow of a drug into, through and between a system of compartments. The compartment of greatest interest to us will be the central compartment, denoted by q_c. This central compartment may be connected with one or more peripheral compartments, denoted by q_p1, ..., q_pn. For ease of exposition, we abuse this notation by denoting the drug concentration in each compartment by the compartment name. We seek to solve numerically the resulting ODE system for said concentrations, q_c, q_p1, ..., q_pn.

The drug may be introduced to the system in different ways; we consider two such dosing types, namely intravenous and subcutaneous dosing types. In the intravanous case, the drug is introduced directly into the central compartment, whereas in the subcutaneous case, the drug enters an initial compartment before being admitted to the central compartment. We denote this initial compartment in the latter case by q_0.

In seeking to achieve a certain drug cincentration in the system's compartments (the central compartment, in particular), a doctor adopts a dosing protocol, that is, he/she introduces the drug to the system (as described in the previous paragraph), following a prespecified pattern over a given time period. For example, the doctor might add the drug at a constant rate throughout the period (which we call a continuous protocol); alternatively, he/she might administer the drug in a short burst or several bursts, separated by pauses (which we call an instantaneous protocol). The dosing protocol is codified in a function Dose(t), e.g. Dose(t) = constant > 0 for a continuous protocol.

