package com.example.restservice;

public class InventoryItem {

	private final String productid;
	private final int qty;

	public InventoryItem(String productid, int qty) {
		this.productid = productid;
		this.qty = qty;
	}

	public String getId() {
		return productid;
	}

	public int getQty() {
		return qty;
	}

	@Override
	public String toString() {
		return "InventoryItem [productid=" + productid + ", qty=" + qty + "]";
	}
}
