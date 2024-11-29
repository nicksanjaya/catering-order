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
    
    # Nilai awal
    harga_ayam = 0
    ayam_min = 1
    ayam_max = 1
    harga_daging = 0
    daging_min = 1
    daging_max = 1
    harga_ikan = 0
    ikan_min = 0
    ikan_max =0
    harga_telur = 0
    telur_min = 0
    telur_max = 0
    harga_special = 0
    special_min = 0
    special_max = 0
    
    
    with st.container():
        col_a = st.columns(1)
        with col_a:
            harga_ayam = st.number_input('Harga Ayam Per Porsi', value=harga_ayam)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            ayam_min = st.number_input('Ayam (Min)', value=ayam_min)
        with col2:
            ayam_max = st.number_input('Ayam (Pcs)', value=ayam_max)  
 
    with st.container():
        col_d = st.columns(1)
        with col_d:
            harga_daging = st.number_input('Harga Daging Per Porsi', value=harga_daging)
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            daging_min = st.number_input('Daging (Min)', value=daging_min)
        with col4:
            daging_max = st.number_input('Daging (Max)', value=daging_max)

    with st.container():
        col_i = st.columns(1)
        with col_i:
            harga_ikan = st.number_input('Harga Ikan Per Porsi', value=harga_ikan)
    with st.container():
        col5, col6 = st.columns(2)
        with col5:
            ikan_min = st.number_input('Ikan (Min)', value=ikan_min)
        with col6:
            ikan_max = st.number_input('Ikan (Max)', value=ikan_max)

    with st.container():
        col_t = st.columns(1)
        with col_t:
            harga_telur = st.number_input('Harga Telur Per Porsi', value=harga_telur)
    with st.container():
        col7, col8 = st.columns(2)
        with col7:
            telur_min = st.number_input('Telur (Min)', value=telur_min)
        with col8:
            telur_max = st.number_input('Telur (Max)', value=telur_max)

    with st.container():
        col_s = st.columns(1)
        with col_s:
            harga_special = st.number_input('Harga Special Per Porsi', value=harga_special)
    with st.container():
        col9, col10 = st.columns(2)
        with col9:
            special_min = st.number_input('Special (Min)', value=special_min)
        with col10:
            special_max = st.number_input('Special (Max)', value=special_max)
    
    st.markdown('---'*10)
    
    # Membuat modelnya
    model = pyo.ConcreteModel()

    # Mendefinisikan variabelnya
    model.a = pyo.Var(bounds=(ayam_min,ayam_max))
    model.d = pyo.Var(bounds=(daging_min,daging_max))
    model.i = pyo.Var(bounds=(ikan_min, ikan_max))
    model.t = pyo.Var(bounds=(telur_min, telur_max))
    model.s = pyo.Var(bounds=(special_min, special_max))
    
    # Mendefinisikan namavariabel baru untuk memudahkan penulisan
    a = model.a
    d = model.d
    i = model.i
    t = model.t
    s = model.s
    
    # Mendefinisikan fungsi pembatas
    model.C1 = pyo.Constraint(expr = 18000*a+15000*d+10000*i+13000*t+12000*s<=7000000)
    model.C2 = pyo.Constraint(expr = a+d+i+t+s==400)
    model.C3 = pyo.Constraint(expr = a>=0)
    model.C4 = pyo.Constraint(expr = d>=0)
    model.C5 = pyo.Constraint(expr = i>=0)
    model.C6 = pyo.Constraint(expr = t>=0)
    model.C7 = pyo.Constraint(expr = s>=0)

    # Mendefinisikan fungsi tujuan
    model.obj = pyo.Objective(expr = 18000*a+15000*d+10000*i+13000*t+12000*s<=7000000, sense=maximize)


    # Mendefinisikan solvernya (pada bagian ini kita bisa memilih 'gurobi', atau 'glpk')
    opt = SolverFactory('glpk')
    
    # Menjalankan optimasinya
    results = opt.solve(model)
    
    # Menyimpan hasilnya
    a_value = pyo.value(a)
    d_value = pyo.value(d)
    i_value = pyo.value(i)
    t_value = pyo.value(t)
    s_value = pyo.value(s)
    z_value = pyo.value(model.obj)
    
    st.markdown('---'*10)
    
    st.write('<center><b><h3>Ayam= ', a_value,'</b></h3>', unsafe_allow_html=True)
    st.write('<center><b><h3>Daging= ', d_value,'</b></h3>', unsafe_allow_html=True)
    st.write('<center><b><h3>Ikan= ', i_value,'</b></h3>', unsafe_allow_html=True)
    st.write('<center><b><h3>Telur= ', t_value,'</b></h3>', unsafe_allow_html=True)
    st.write('<center><b><h3>Special= ', s_value,'</b></h3>', unsafe_allow_html=True)
    st.write('<center><b><h3>Total= ', z_value,'</b></h3>', unsafe_allow_html=True)

if __name__ == '__main__':
	main() 
