# Mebgimpor library
import streamlit as st
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Membuat judul
st.title('NICKI SANJAYA')

# Menambah subheader
st.subheader('Selamat datang di Data Science Deployment')

# Ini merupakan fungsi utama
def main():
    
    #st.markdown('Ayam')
    # Nilai awal
    ayam_min = 1
    ayam_max = 1
    daging_min = 1
    daging_max = 1
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            ayam_min = st.number_input('Ayam (Min)', value=ayam_min)
        with col2:
            ayam_max = st.number_input('Ayam (Pcs)', value=ayam_max)  
    
    #st.markdown('Daging')
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            daging_min = st.number_input('Daging (Min)', value=daging_min)
        with col4:
            daging_max = st.number_input('Daging (Max)', value=daging_max)

    
    
    st.markdown('---'*10)
    
    # Membuat modelnya
    model = pyo.ConcreteModel()

    # Mendefinisikan variabelnya
    model.x = pyo.Var(bounds=(ayam_min,ayam_max))
    model.y = pyo.Var(bounds=(daging_min,daging_max))
    
    # Mendefinisikan namavariabel baru untuk memudahkan penulisan
    x = model.x
    y = model.y
    
    
    # Mendefinisikan fungsi pembatas
    model.C1 = pyo.Constraint(expr = -x + 2*y <= 8)
    model.C2 = pyo.Constraint(expr = 2*x + y <= 14)
    model.C3 = pyo.Constraint(expr = 2*x - y <= 10)

    # Mendefinisikan fungsi tujuan
    model.obj = pyo.Objective(expr = x + y, sense=maximize)


    # Mendefinisikan solvernya (pada bagian ini kita bisa memilih 'gurobi', atau 'glpk')
    opt = SolverFactory('glpk')
    
    # Menjalankan optimasinya
    results = opt.solve(model)
    
    # Menyimpan hasilnya
    x_value = pyo.value(x)
    y_value = pyo.value(y)
    z_value = pyo.value(model.obj)
    
    st.markdown('---'*10)
    
    st.write('<center><b><h3>Ayam= ', x_value,'</b></h3>', unsafe_allow_html=True)
    st.write('<center><b><h3>Daging= ', y_value,'</b></h3>', unsafe_allow_html=True)
    st.write('<center><b><h3>Total= ', z_value,'</b></h3>', unsafe_allow_html=True)

if __name__ == '__main__':
	main() 
