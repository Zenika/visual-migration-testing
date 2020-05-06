describe('services', function() {

 it('Test services page', function() {

    cy.viewport(1920, 932)
 
    cy.visit('http://coalescent.brandonsavage.net/')
 
    cy.get('.page-inner > .main-menu > .subnav > li:nth-child(1) > a').click()
 
    cy.visit('http://coalescent.brandonsavage.net/index.php/index/how-it-works')
 
 })

})

