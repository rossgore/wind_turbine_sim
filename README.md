# wind_turbine_sim
Wind Turbine Simulation for CyberWind Project

# Wind Turbine

Implement model of variable pitch wind turbine

## Description

The Wind Turbine block models the steady-state power characteristics of a wind turbine. The stiffness of the drive train is infinite and the friction factor and the inertia of the turbine must be combined with those of the generator coupled to the turbine. The output power of the turbine is given by the following equation:

$$ P_{m}=c_{p}(\lambda, \beta) \frac{\rho A}{2} v_{\mathrm{wind}}^{3}, $$

where:

| Symbol | Description |
|--------|-------------|
| $$P_{m}$$ | Mechanical output power of the turbine (W) |
| $$c_{p}$$ | Performance coefficient of the turbine |
| $$\rho$$ | Air density $$\left(\mathrm{kg} / \mathrm{m}^{3}\right)$$ |
| $$A$$ | Turbine swept area $$\left(\mathrm{m}^{2}\right)$$ |
| $$v_{\text {wind }}$$ | Wind speed (m/s) |
| $$\lambda$$ | Tip speed ratio of the rotor blade tip speed to wind speed |
| $$\beta$$ | Blade pitch angle (deg) |

Equation 1 can be normalized. In the per unit (pu) system we have:

$$ P_{m_{-} \mathrm{pu}}=k_{p} c_{p_{-} \mathrm{pu}} v_{\text {wind_pu }}^{3}, $$

where:

| Symbol | Description |
|--------|-------------|
| $$P_{m_{-} \mathrm{pu}}$$ | Power in pu of nominal power for particular values of $$\rho$$ and $$A$$ |
| $$c_{p_{-} \mathrm{pu}}$$ | Performance coefficient in pu of the maximum value of $$c_{p}$$ |
| $$v_{\text {wind_pu }}$$ | Wind speed in pu of the base wind speed. The base wind speed is the mean value of the expected wind speed in $$\mathrm{m} / \mathrm{s}$$. |
| $$k_{p}$$ | Power gain for $$c_{p-p u}=1$$ pu and $$v_{\text {wind_pu }}=1 \mathrm{pu}, k_{p}$$ is less than or equal to 1 |

A generic equation is used to model $$c_{p}(\lambda, \beta)$$. This equation, based on the modeling turbine characteristics, is:

$$ c_{p}(\lambda, \beta)=c_{1}\left(c_{2} / \lambda_{i}-c_{3} \beta-c_{4}\right) e^{-c_{5} / \lambda_{i}}+c_{6} \lambda $$

with:

$$ \frac{1}{\lambda_{i}}=\frac{1}{\lambda+0.08 \beta}-\frac{0.035}{\beta^{3}+1} $$

The coefficients $$c_{1}$$ to $$c_{6}$$ are: $$c_{1}=0.5176, c_{2}=116, c_{3}=0.4, c_{4}=5, c_{5}=21$$ and $$c_{6}=0.0068$$.

The maximum value of $$c_{p}\left(c_{p \max }=0.48\right)$$ is achieved for $$\beta=0$$ degrees and for $$\lambda=8.1$$. This particular value of $$\lambda$$ is defined as the nominal value ( $$\lambda_{\text {_nom }}$$ )[1].

## Ports

### Input

- Generator speed (pu): Generator speed based on the nominal speed of the generator, specified as a scalar, in pu.
- Pitch angle (deg): Pitch angle, specified as a scalar
- Wind speed (m/s): Wind speed, specified as a nonnegative scalar, in m/s.

### Output

- Tm(pu): Mechanical torque of the wind turbine, returned as a scalar, in pu of the nominal generator torque. The nominal torque of the generator is based on the nominal generator power and speed.

## Parameters

- Nominal mechanical output power: 1.5e6 (default) | nonnegative scalar
- Base power of the electrical generator: 1.5e6/0.9 (default) | positive scalar
- Power gain kp: 0.73 (default) | scalar between 0 and 1
- Base rotational speed: 1.2 (default) | positive scalar
- Pitch angle beta: 0 (default) | nonnegative scalar

## References

[1] Siegfried Heier, "Grid Integration of Wind Energy Conversion Systems," John Wiley & Sons Ltd, 1998, ISBN 0-471-97143-X

## Extended Capabilities

C/C++ Code Generation: Generate C and C++ code using Simulink® Coder™.

## Version History

Introduced in R2006a

## See Also

Wind Turbine Induction Generator (Phasor Type) | Wind Turbine DoublyFed Induction Generator (Phasor Type)
