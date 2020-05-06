describe('contact', function() {

 it('Test contact page', function() {

    cy.viewport(1920, 932)
 
    cy.visit('http://coalescent.brandonsavage.net/')
 
    cy.get('body > .site-wrap > .header > .page-center > .page-inner').click()
 
    cy.get('.page-inner > .main-menu > .subnav > li:nth-child(4) > a').click()
 
    cy.visit('http://coalescent.brandonsavage.net/index.php/index/contact')
 
 })

})

