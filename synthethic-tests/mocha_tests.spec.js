var expect  = require("chai").expect;
var request = require("request");

describe("My Inventory API", function() {

  describe("Get Inventory List", function() {

    var url = "SERVICE_URL/inventory";

    it("returns status 200", function(done) {
      request(url, function(error, response, body) {
        if (error) {
           throw error;
        }
        expect(response.statusCode).to.equal(200);
        done();
      })
    });

    it("inventory dictionary length should be 1", function(done) {
      request(url, function(error, response, body) {
        if (error) {
           throw error;
        }
        const obj = JSON.parse(body)
        expect(obj).to.be.an.instanceOf(Object);
        const dictionary_length = Object.keys(obj).length;
        expect(dictionary_length == 1);
        done();
      })
    });
  });

  describe("Get Incorrect Inventory Item", function() {

    var url = "SERVICE_URL/inventory/ABC";

    it("returns status 200", function(done) {
      request(url, function(error, response, body) {
        if (error) {
           throw error;
        }
        expect(response.statusCode).to.equal(200);
        done();
      })
    });

    it("returns quantity as -1", function(done) {
      request(url, function(error, response, body) {
        if (error) {
           throw error;
        }
        const obj = JSON.parse(body)
        expect(parseInt(obj["qty"])).to.equal(-1);
        expect(obj["productid"]).to.equal("ABC");
        done();
      })
    });

  });

  describe("Get Inventory Item", function() {

    var url = "SERVICE_URL/inventory/I-1";

    it("returns status 200", function(done) {
      request(url, function(error, response, body) {
        if (error) {
           throw error;
        }
        expect(response.statusCode).to.equal(200);
        done();
      })
    });

    it("returns specific inventory items with productid as I-1", function(done) {
      request(url, function(error, response, body) {
        if (error) {
           throw error;
        }
        const obj = JSON.parse(body)
        expect(obj["productid"]).to.equal("I-1");
        done();
      })
    });
  });
});
