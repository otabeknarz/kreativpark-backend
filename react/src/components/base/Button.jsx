import Button from '@mui/material/Button';

export default function ButtonUsage({ text, onClick, onClickProps, color }) {
  return <Button variant="contained" onClick={() => onClick(onClickProps)} color={color}>{text}</Button>;
}
