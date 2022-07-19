package com.example.restservice;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@RestController
public class RestServiceController {

	private static final Logger log = LoggerFactory.getLogger(RestServiceController.class);

	private static final String template = "Hello, %s!";
	private final AtomicLong counter = new AtomicLong();
	static List<InventoryItem> inventorylist = new ArrayList<InventoryItem>();
	static {
		inventorylist.add(new InventoryItem("I-1",10));
		inventorylist.add(new InventoryItem("I-2",20));
		inventorylist.add(new InventoryItem("I-3",30));
	}

	@GetMapping("/greeting")
	public Greeting greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
		return new Greeting(counter.incrementAndGet(), String.format(template, name));
	}
	
	@GetMapping("/healthy")
	public String healthy() {
		return "All Izz Well";
	}

	@GetMapping("/inventory")
	public List<InventoryItem> inventorylist() {
		return inventorylist;
	}

	@GetMapping("/inventory/{productid}")
	public Object inventory(@PathVariable String productid) {
		if (productid.equals("")) {
			return inventorylist;
		} 
		else {
			Boolean bFound = false;
			InventoryItem item = null;

            for (InventoryItem inventoryItem : inventorylist) {
				if (inventoryItem.getId().equals(productid)) {
					bFound = true;
					item = inventoryItem;
				}
			}
			if (!bFound) {
				log.warn("Received inventory request for incorrect productid:" +productid);
				item = new InventoryItem(productid,-1);
			}
			return item;
		}
	}
}
