function Minv = Matrix_Inverse(A)
    [m,n] = size(A);
    if m ~= n
        error(' Non-Approriate Dimentions: Matrix Must Be Squared')
    end


    AugM = [A eye(n)];
    for i = 1:n


        [~, max_row] = max(abs(AugM(i:end,i)));
        max_row = max_row + i  -1;

        if AugM(max_row, i ) == 0
            error('Matrix is Singular');
        end

        if max_row ~= i
            AugM([i,max_row], :) = AugM([max_row,i],:);
        end


        AugM(i,:) = AugM(i,:) / AugM(i,i);
        for j = 1:n
            if j ~= i
                AugM(j,:) = AugM(j,:) - AugM(j,i) * AugM(i,:);
            end
        end
    end
    A = AugM(:, n+1:end)
end
