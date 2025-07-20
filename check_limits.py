
def battery_is_ok(temperature, soc, charge_rate):
  out_of_range=( 
    (temperature < 0 or temperature > 45) or
    (soc < 20 or sor > 80)
    (charge_rate > 0.8)
  )
  if out_of_range:
    print('Battery parameter out of range!'0)
    return False

  return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
