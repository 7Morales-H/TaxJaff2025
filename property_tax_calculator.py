import streamlit as st

def calculate_property_tax(property_value, total_tax_rate, school_budget_percentage):
    """
    Calculate the total property tax and its distribution across various categories.
    
    Parameters:
    - property_value: The property value entered by the user
    - total_tax_rate: The fixed total tax rate per $1,000 of valuation (32.80 / 1000)
    - school_budget_percentage: The percentage of the total tax allocated to the school portion (changes based on budget)
    
    Returns:
    - A dictionary containing the total tax and tax distribution by category
    """
    # Total tax calculated based on fixed tax rate
    total_tax = property_value * total_tax_rate
    
    # School portion changes based on the school budget percentage
    school_tax = total_tax * school_budget_percentage
    
    # Other portions (municipal, state education, county) remain fixed
    municipal_tax = total_tax * 0.32
    state_ed_tax = total_tax * 0.06
    county_tax = total_tax * 0.12
    
    # Update total tax to reflect the school tax portion correctly
    total_tax_with_school_change = school_tax + municipal_tax + state_ed_tax + county_tax
    
    return {
        "Total Tax": total_tax_with_school_change,
        "School Tax": school_tax,
        "Municipal Tax": municipal_tax,
        "State Ed Tax": state_ed_tax,
        "County Tax": county_tax
    }

def display_tax_comparison(property_value):
    # Fixed total tax rate per $1,000 valuation
    total_tax_rate = 32.80 / 1000
    
    # Budget values (in dollars)
    current_budget = 33760452
    new_budget = 30760452
    default_budget = 33858458
    
    # Calculate the school portion percentage for each budget
    current_school_percentage = current_budget / (current_budget + new_budget + default_budget)
    new_school_percentage = new_budget / (current_budget + new_budget + default_budget)
    default_school_percentage = default_budget / (current_budget + new_budget + default_budget)
    
    # Calculate taxes for each budget scenario separately
    current_tax = calculate_property_tax(property_value, total_tax_rate, current_school_percentage)
    default_tax = calculate_property_tax(property_value, total_tax_rate, default_school_percentage)
    new_tax = calculate_property_tax(property_value, total_tax_rate, new_school_percentage)
    
    # Display results for each budget scenario separately
    st.subheader("✅ Current Property Tax (Based on Current Budget):")
    st.write(f"Total Tax: ${current_tax['Total Tax']:,.2f}")
    st.write(f"School Tax: ${current_tax['School Tax']:,.2f}, Municipal Tax: ${current_tax['Municipal Tax']:,.2f}, State Ed Tax: ${current_tax['State Ed Tax']:,.2f}, County Tax: ${current_tax['County Tax']:,.2f}")
    
    st.subheader("✅ Default Budget Property Tax:")
    st.write(f"Total Tax: ${default_tax['Total Tax']:,.2f}")
    st.write(f"School Tax: ${default_tax['School Tax']:,.2f}, Municipal Tax: ${default_tax['Municipal Tax']:,.2f}, State Ed Tax: ${default_tax['State Ed Tax']:,.2f}, County Tax: ${default_tax['County Tax']:,.2f}")
    
    st.subheader("✅ New Budget Property Tax:")
    st.write(f"Total Tax: ${new_tax['Total Tax']:,.2f}")
    st.write(f"School Tax: ${new_tax['School Tax']:,.2f}, Municipal Tax: ${new_tax['Municipal Tax']:,.2f}, State Ed Tax: ${new_tax['State Ed Tax']:,.2f}, County Tax: ${new_tax['County Tax']:,.2f}")
    
    st.subheader("✅ Tax Changes Compared to Different Budgets:")
    st.write(f"Change from Current to Default Budget: ${default_tax['Total Tax'] - current_tax['Total Tax']:,.2f}")
    st.write(f"Change from Current to New Budget: ${new_tax['Total Tax'] - current_tax['Total Tax']:,.2f}")

# Streamlit Input for Property Value
st.title("Property Tax Calculator for Jaffrey, NH")
property_value = st.number_input("Enter your property value ($)", min_value=0, value=205000, step=1000)

# Display tax comparison
if property_value:
    display_tax_comparison(property_value)
