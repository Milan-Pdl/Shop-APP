import streamlit as st

# Price list
khakura = {"chauchau": 100, "cofee": 50, "momo": 120,"Chowmin":100,"Cold_cofee":100}

# Initialize order list in session state
if 'orders' not in st.session_state:
    st.session_state.orders = []

def display_menu():
    st.subheader("🍽️ Menu")
    for item, price in khakura.items():
        st.write(f"**{item.title()}** - Rs. {price}")

def place_order():
    st.subheader("📝 Place Your Order")
    name = st.text_input("Enter your name").strip().lower()
    item = st.selectbox("Select your order", list(khakura.keys()))
    quantity = st.number_input("Enter quantity", min_value=1, step=1)

    if st.button("Place Order"):
        st.session_state.orders.append({
            'name': name,
            'item': item,
            'quantity': quantity
        })
        st.success(f"{quantity}x {item} added for {name}")

def add_more_items():
    st.subheader("➕ Add More Items")
    name = st.text_input("Enter your name to add more items").strip().lower()

    if name:
        item = st.selectbox("Select item to add", list(khakura.keys()), key="add_item")
        quantity = st.number_input("Enter quantity", min_value=1, step=1, key="add_quantity")

        if st.button("Add Item"):
            st.session_state.orders.append({
                'name': name,
                'item': item,
                'quantity': quantity
            })
            st.success(f"{quantity}x {item} added for {name}")

def generate_bill():
    st.subheader("💰 Pay Your Bill")
    name = st.text_input("Enter your name to get the bill").strip().lower()

    if st.button("Generate Bill"):
        user_orders = [order for order in st.session_state.orders if order['name'] == name]
        
        if not user_orders:
            st.error("❌ No orders found with that name.")
            return

        total = 0
        st.write(f"### Bill for {name.title()}")
        for order in user_orders:
            item_price = khakura.get(order['item'], 0)
            subtotal = item_price * order['quantity']
            total += subtotal
            st.write(f"{order['quantity']} x {order['item'].title()} = Rs. {subtotal}")

        st.success(f"✅ Total Amount Due: Rs. {total}")

# --- Streamlit UI ---
st.title("🛒 Suman Dai Ko Pasal")
menu = st.sidebar.radio("Choose Action", ["📋 Menu", "📝 Place Order", "➕ Add More Items", "💰 Pay Bill"])

if menu == "📋 Menu":
    display_menu()
elif menu == "📝 Place Order":
    place_order()
elif menu == "➕ Add More Items":
    add_more_items()
elif menu == "💰 Pay Bill":
    generate_bill()
