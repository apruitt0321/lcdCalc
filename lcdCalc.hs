import System.Environment

parseArgs :: String -> Int
parseArgs x 
    | x == ['0'] = 1
    | otherwise = read x

testDiv :: Int -> Int -> Bool
testDiv 0 y = testDiv 1 y
testDiv x y
    | x `mod` y == 0 = True
    | otherwise = False

lcd :: [Int] -> Int -> Int 
lcd (x) 0 = lcd x 1
lcd (x) y 
    | False `elem` q = lcd x (y+1)
    | otherwise = y
    where q = map (testDiv y) x

main = do
    a <- getArgs
    let y = map parseArgs a  
    print $ lcd y 1
