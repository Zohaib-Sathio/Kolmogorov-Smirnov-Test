import streamlit as st
import numpy as np
import random


def ks_critical_value(n, alpha):
    c_alpha_dict = {0.001: 1.95, 0.01: 1.63, 0.02: 1.52, 0.05: 1.36, 0.10: 1.22, 0.15: 1.14, 0.2: 1.07}
    
    if alpha not in c_alpha_dict:
        raise ValueError(f"Alpha {alpha} not supported. Choose from {list(c_alpha_dict.keys())}")
    
    c_alpha = c_alpha_dict[alpha]
    
    # Calculate D_alpha
    D_alpha = c_alpha / np.sqrt(n)
    return D_alpha

# Function to generate random numbers and perform the KS test
def generate_random(X0, a, c, m, n, alpha):
    random_numbers = [X0]
    for _ in range(1, n+1):
        Xn = (a * random_numbers[-1] + c) % m
        random_numbers.append(Xn)
    
    random_numbers = random_numbers[1:]

    random_numbers_normalized = np.array(random_numbers) / m
    sorted_numbers = np.sort(random_numbers_normalized)
    edf = np.arange(1, n + 1) / n
    cdf_uniform = edf - sorted_numbers
    te = []
    for i in range(n):
        te.append(sorted_numbers[i]- (i/n))

    max_edf = max(cdf_uniform)
    max_te = max(te)

    D = np.max(int(max_edf), int(max_te))
    if max_edf > max_te:
        D = max_edf
    elif max_te >= max_edf:
        D = max_te

    D_alpha = ks_critical_value(n, alpha)
    # print(D_alpha)
    reject_null = D > D_alpha

    return random_numbers, random_numbers_normalized, sorted_numbers, edf, cdf_uniform, D, reject_null, D_alpha

# Function to generate random parameters
def generate_random_params():
    X0 = random.randint(1, 1000) 
    a = random.randint(1, 1000)  
    c = random.randint(0, 1000)   
    m = random.randint(10, 500)  
    n = random.randint(10, 100)
    return X0, a, c, m, n


st.title("Random Number Generator and KS Test")

st.sidebar.header("Enter Parameters or Generate Random Ones")

alpha = st.sidebar.selectbox("Select significance level (alpha):", options=[0.001, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2])

if st.sidebar.button("Generate Random Parameters"):
    X0, a, c, m, n = generate_random_params()
    st.sidebar.write(f"Generated Parameters: X0={X0}, a={a}, c={c}, m={m}, n={n}")

    if True:
        random_numbers, random_numbers_normalized, sorted_numbers, edf, cdf_uniform, D, reject_null, D_alpha = generate_random(X0, a, c, m, n, alpha)

        st.write('## Summarized results: ')

        st.write("### Generated Random Numbers:")
        st.write(str(random_numbers))

        st.write(f"### D_alpha: {D_alpha:.4f}")

        st.write(f"### KS Statistic (D): {D:.4f}")

        st.write(f"### Reject Null Hypothesis (at 5% significance level): {reject_null}")

        if reject_null:
            st.write("The KS test **rejects** the null hypothesis, indicating that the generated random numbers do not follow a uniform distribution.")
        else:
            st.write("The KS test **does not reject** the null hypothesis, indicating that the generated random numbers follow a uniform distribution.")

        st.write("### ALL STEPS:")
        
        st.write("### Generated Random Numbers:")
        st.write(f"Random Numbers: {random_numbers}")

        st.write("### Normalized Random Numbers (for KS Test):")
        st.write(random_numbers_normalized)

        st.write("### Sorted Normalized Random Numbers (Empirical Distribution Function - EDF):")
        st.write(sorted_numbers)

        st.write("### Empirical Distribution Function (EDF):")
        st.write(edf)

        st.write("### Cumulative Distribution Function (CDF) for Uniform Distribution:")
        st.write(cdf_uniform)

        st.write(f"### KS Statistic (D): {D:.4f}")

        st.write(f"### Reject Null Hypothesis (at 5% significance level): {reject_null}")

        if reject_null:
            st.write("The KS test **rejects** the null hypothesis, indicating that the generated random numbers do not follow a uniform distribution.")
        else:
            st.write("The KS test **does not reject** the null hypothesis, indicating that the generated random numbers follow a uniform distribution.")

else:
    X0 = st.sidebar.number_input("Initial seed (X0)", min_value=1, value=189)
    a = st.sidebar.number_input("Multiplier (a)", min_value=1, value=97)
    c = st.sidebar.number_input("Increment (c)", min_value=0, value=107)
    m = st.sidebar.number_input("Modulus (m)", min_value=1, value=203)
    n = st.sidebar.number_input("Number of random numbers to generate (n)", min_value=10, value=100)

    if st.sidebar.button("Generate and Test"):
        random_numbers, random_numbers_normalized, sorted_numbers, edf, cdf_uniform, D, reject_null, D_alpha = generate_random(X0, a, c, m, n, alpha)


        st.write('## Summarized results: ')

        st.write("### Generated Random Numbers:")
        st.write(f"Random Numbers: {random_numbers}")

        st.write(f"### D_alpha: {D_alpha:.4f}")

        st.write(f"### KS Statistic (D): {D:.4f}")

        st.write(f"### Reject Null Hypothesis : {reject_null}")

        if reject_null:
            st.write("The KS test **rejects** the null hypothesis, indicating that the generated random numbers do not follow a uniform distribution.")
        else:
            st.write("The KS test **does not reject** the null hypothesis, indicating that the generated random numbers follow a uniform distribution.")

        st.write("### ALL STEPS:")

        st.write("### Generated Random Numbers:")
        st.write(random_numbers)

        st.write("### Normalized Random Numbers (for KS Test):")
        st.write(random_numbers_normalized)

        st.write("### Sorted Normalized Random Numbers (Empirical Distribution Function - EDF):")
        st.write(sorted_numbers)

        st.write("### Empirical Distribution Function (EDF):")
        st.write(edf)

        st.write("### Cumulative Distribution Function (CDF) for Uniform Distribution:")
        st.write(cdf_uniform)

        st.write(f"### KS Statistic (D): {D:.4f}")

        st.write(f"### Reject Null Hypothesis (at 5% significance level): {reject_null}")

        if reject_null:
            st.write("The KS test **rejects** the null hypothesis, indicating that the generated random numbers do not follow a uniform distribution.")
        else:
            st.write("The KS test **does not reject** the null hypothesis, indicating that the generated random numbers follow a uniform distribution.")

