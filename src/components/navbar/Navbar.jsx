import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import './Navbar.css'

function NavScrollExample() {
    return (
        <Navbar fixed="top" bg="dark" data-bs-theme="dark" className='navbar__main'>
            <Container fluid>
                <Navbar.Brand href="#" className='navbar__brand'>e z m</Navbar.Brand>
                <Navbar.Toggle aria-controls="navbarScroll" />
                <Form className="d-flex ">
                        <Form.Control
                            type="search"
                            placeholder="search an asset..."
                            className="me-2"
                            aria-label="Search"
                        />
                        <Button variant="outline-light" className='navbar__search__button'>search</Button>
                    </Form>
                <Navbar.Collapse id="navbarScroll">
                    <Nav
                        className="me-auto my-2 my-lg-0"
                        style={{ maxHeight: '100px' }}
                        navbarScroll
                    >
                        <Nav.Link href="#home" className='navbar__home-button'>home</Nav.Link>
                        <Nav.Link href="#insights" className='navbar__insights-button'>insights</Nav.Link>
                        <Nav.Link href="#model_specifications" className='navbar__model-button'>model specification</Nav.Link>
                        <Nav.Link href="#about" className='navbar__about-button'>about</Nav.Link>
                    </Nav>

                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default NavScrollExample;