#function that adds two given values
r_add <- function(x,y) {
  if(!is.numeric(x)||!is.numeric(y)) stop("Non numeric value passed")
  x+y
}

#function that subtracts two given values
r_subtract <- function(x,y) {
  if(!is.numeric(x)||!is.numeric(y)) stop("Non numeric value passed")
  x-y
}

#function that multiplys two given values
r_multiply <- function(x,y) {
  if(!is.numeric(x)||!is.numeric(y)) stop("Non numeric value passed")
  x*y
}

#function that divides two values
r_divide <- function(x,y) {
  if(!is.numeric(x)||!is.numeric(y)) stop("Non numeric value passed")
  x/y
}

#function that gives the squareroot of a value
r_squareroot <- function(x) {
  if(!is.numeric(x)) stop("Non numeric value passed")
  sqrt(x)
}

#function that gives the sine of a value
r_sin <- function(x) {
  if(!is.numeric(x)) stop("Non numeric value passed")
  sin(x)
}

#function that gives the cosine of a value
r_cos <- function(x) {
  if(!is.numeric(x)) stop("Non numeric value passed")
  cos(x)
}

#function that gives the tangent of a value
r_tan <- function(x) {
  if(!is.numeric(x)) stop("Non numeric value passed")
  tan(x)
}

#function that gives the log base 10 of a value
r_log10 <- function(x) {
  if(!is.numeric(x)) stop("Non numeric value passed")
  log10(x)
}

#function that gives the exponent of x given y
r_expo <- function(x,y) {
  if(!is.numeric(x)||!is.numeric(y)) stop("Non numeric value passed")
  x^y
}

