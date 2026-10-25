function x = Gauss_Jordan(A,b)
    [m,n] = size(A);
    AugM = [A b]
    for i = 1:n
        AugM(i,:) = AugM(i,:) / AugM(i,i);
        for j = 1:n
            if j ~= i
                AugM(j,:) = AugM(j,:) - AugM(j,i) * AugM(i,:);
            end
        end
    end
    x = AugM(:,end);
    display(x)
end
