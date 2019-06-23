import System.Environment

gcf x 0 = x
gcf x y = gcf y (x `mod` y)

lcd :: [Int] -> Int
lcd [] = 0
lcd (x:[]) = x
lcd (x:y:xs) = lcd (((x*y) `div` (gcf x y)):xs)

main = do
    a <- getArgs
    let y = map read a
    if 0 `elem` y then putStrLn "Cant use zero"
    else print $ lcd (map abs y)
