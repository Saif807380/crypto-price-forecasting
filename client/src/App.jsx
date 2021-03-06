import "./App.css";
import { Container, Typography, Box, Divider } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

import Bitcoin from "./components/Bitcoin";
import Monero from "./components/Monero";
import Ethereum from "./components/Ethereum";

const useStyles = makeStyles((theme) => ({
  root: {
    minHeight: "80vh",
    marginTop: theme.spacing(4),
    marginBottom: theme.spacing(2)
  },
  title: {
    textAlign: "center",
    width: "70%"
  }
}));

const App = () => {
  const classes = useStyles();
  return (
    <Container className={classes.root}>
      <Box display="flex" flexDirection="column" alignItems="center">
        <Typography variant="h4" className={classes.title}>
          Analysis and Forecasting of Cryptocurrency Prices
        </Typography>
      </Box>
      <Divider style={{ marginTop: "16px" }} />
      <Box style={{ paddingTop: "16px" }}>
        <Box style={{ marginBottom: "16px" }}>
          <Bitcoin />
        </Box>
        <Box style={{ marginBottom: "16px" }}>
          <Ethereum />
        </Box>
        <Box style={{ marginBottom: "16px" }}>
          <Monero />
        </Box>
      </Box>
    </Container>
  );
};

export default App;
