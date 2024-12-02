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
    kuota = 0
    budget = 7000000
    harga_ayam = 10000
    ayam_min = 140
    harga_daging = 10000
    daging_min = 80
    harga_ikan = 10000
    ikan_min = 50
    harga_telur = 10000
    telur_min = 50
    harga_special = 10000
    special_min = 0

    with st.container():
        col_k = st.columns(1)
        with col_k[0]:
            kuota = st.number_input('Budget', value=kuota)

    st.markdown('---'*10)
	
    with st.container():
        col_b = st.columns(1)
        with col_b[0]:
            budget = st.number_input('Budget', value=budget)

    st.markdown('---'*10)	
	
    with st.container():
        col_a = st.columns(1)
        with col_a[0]:
            harga_ayam = st.number_input('Harga Ayam Per Porsi', value=harga_ayam)	
    with st.container():
        col1 = st.columns(1)
        with col1[0]:
            ayam_min = st.number_input('Ayam (Min)', value=ayam_min)

    st.markdown('---'*10)
 
    with st.container():
        col_d = st.columns(1)
        with col_d[0]:
            harga_daging = st.number_input('Harga Daging Per Porsi', value=harga_daging)
    with st.container():
        col2= st.columns(1)
        with col2[0]:
            daging_min = st.number_input('Daging (Min)', value=daging_min)

    st.markdown('---'*10)
	
    with st.container():
        col_i = st.columns(1)
        with col_i[0]:
            harga_ikan = st.number_input('Harga Ikan Per Porsi', value=harga_ikan)
    with st.container():
        col3 = st.columns(1)
        with col3[0]:
            ikan_min = st.number_input('Ikan (Min)', value=ikan_min)

    st.markdown('---'*10)

    with st.container():
        col_t = st.columns(1)
        with col_t[0]:
            harga_telur = st.number_input('Harga Telur Per Porsi', value=harga_telur)
    with st.container():
        col4 = st.columns(1)
        with col4[0]:
            telur_min = st.number_input('Telur (Min)', value=telur_min)

    st.markdown('---'*10)

    with st.container():
        col_s = st.columns(1)
        with col_s[0]:
            harga_special = st.number_input('Harga Special Per Porsi', value=harga_special)
    with st.container():
        col5 = st.columns(1)
        with col5[0]:
            special_min = st.number_input('Special (Min)', value=special_min)
    
    st.markdown('---'*10)
    
    # Membuat modelnya
    model = pyo.ConcreteModel()

    # Mendefinisikan variabelnya
    model.a = pyo.Var(bounds=(ayam_min,None))
    model.d = pyo.Var(bounds=(daging_min,None))
    model.i = pyo.Var(bounds=(ikan_min,None))
    model.t = pyo.Var(bounds=(telur_min,None))
    model.s = pyo.Var(bounds=(special_min,None))
    
    # Mendefinisikan namavariabel baru untuk memudahkan penulisan
    a = model.a
    d = model.d
    i = model.i
    t = model.t
    s = model.s
    
    # Mendefinisikan fungsi pembatas
    model.C1 = pyo.Constraint(expr = harga_ayam*a+harga_daging*d+harga_ikan*i+harga_telur*t+harga_special*s<=budget)
    model.C2 = pyo.Constraint(expr = a+d+i+t+s==kuota)
    model.C3 = pyo.Constraint(expr = a>=0)
    model.C4 = pyo.Constraint(expr = d>=0)
    model.C5 = pyo.Constraint(expr = i>=0)
    model.C6 = pyo.Constraint(expr = t>=0)
    model.C7 = pyo.Constraint(expr = s>=0)

    # Mendefinisikan fungsi tujuan
    model.obj = pyo.Objective(expr = harga_ayam*a+harga_daging*d+harga_ikan*i+harga_telur*t+harga_special*s, sense=maximize)


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
