describe('location.json', function () {
  it('should validate as json', function () {
    let content = require('../vocabularies/json-ld/locations.json')
    expect(content).to.be.a('object')
  })

  describe('@graph entries', function () {
    let content = require('../vocabularies/json-ld/locations.json')

    it('should be an array', function () {
      expect(content['@graph']).to.be.a('array')
    })

    describe('each entry', function () {
      it('should be an object ', function () {
        content['@graph'].forEach(function (item) {
          expect(item).to.be.a('object')
        })
      })

      it('should have an @id', function () {
        content['@graph'].forEach(function (item) {
          expect(item['@id']).to.be.a('string')
          expect(item['@id']).to.match(/^nyplLocation:\w+/)
        })
      })

      it('should have 1 or 0 recapCustomerCodes', function () {
        content['@graph'].forEach(function (item) {
          // Only check recapCustomerCode if it's set; Null recap codes are okay
          if (item['nypl:recapCustomerCode']) {
            expect(item['nypl:recapCustomerCode']).to.be.a('object')
          }
        })
      })
    })
  })
})
