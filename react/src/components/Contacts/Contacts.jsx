import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

function Contacts() {
    return (
        <section className="contact container" id="contact">
            <h1><i className="fa-solid fa-address-book"></i> Bog'lanish</h1>
            <h3>Xabar qoldiring</h3>
            <Box
                // id="contact-form"
                component="form"
                // sx={{'& > :not(style)': {m: 1, width: '25ch'}}}
                noValidate
                // autoComplete="off"
            >
                <TextField id="outlined-basic" label="Ism Familiya" variant="outlined"/>
                <TextField id="outlined-basic" label="Email" variant="outlined"/>
                <button type="submit" className="btn-primary"><i className="fa-solid fa-paper-plane"></i> Jo'natish
                </button>
            </Box>
        </section>

    )
}

export default Contacts;